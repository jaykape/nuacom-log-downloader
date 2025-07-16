import requests
import os
import time
from config import TOKEN, SAVE_FOLDER, FILTERS 
from urllib.parse import urlencode, quote_plus

if not os.path.exists(SAVE_FOLDER):
    os.makedirs(SAVE_FOLDER)

page = 1
more = True

def clean(s):
    return ''.join(c if c.isalnum() or c in ('-', '_') else '_' for c in str(s))

def build_url(page):
    base_url = 'https://api.nuacom.ie/v1/call_logs'
    params = {'page': page}

    for key, value in FILTERS.items():
        if value:
            params[key] = value


    return f"{base_url}?{urlencode(params, quote_via=quote_plus)}"


while more:
    url = build_url(page)
    headers = {
        'X-Nuacom-Token': TOKEN
    }

    print(f"Fetching data from page {page}: {url}")
    response = requests.get(url, headers=headers)
    data = response.json()

    calls = data.get('_embedded', [])
    if not calls:
        break

    for call in calls:
        if 'recording' in call:
            try:
                recording_url = f'https://api.nuacom.ie/v1/recording?call_id={call["call_id"]}&format=mp3'
                recording_response = requests.get(recording_url, headers=headers)

                call_date = call.get('call_date', 'unknown')
                from_name = call.get('from_name') or call.get('from_ext_name') or 'unknown'
                to_name = call.get('to_name') or call.get('to_ext_name') or 'unknown'
                from_number = call.get('from', 'unknown')
                to_number = call.get('to', 'unknown')

                file_name = f"{call_date}_{from_name}_{from_number}_to_{to_name}_{to_number}.mp3"

                file_name = clean(file_name)

                # limit length to avoid OS error
                if len(file_name) > 150:
                    file_name = file_name[:150] + '.mp3'

                file_path = os.path.join(SAVE_FOLDER, file_name)

                with open(file_path, 'wb') as file:
                    file.write(recording_response.content)

                print(f"Downloaded {file_name}")
                time.sleep(0.5)

            except Exception as err:
                print(f"Failed to download call {call.get('call_id', 'N/A')}: {err}")

    more = '_links' in data and 'next' in data['_links']
    page += 1

print("Download complete")
