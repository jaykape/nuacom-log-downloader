
TOKEN = ''                                  #Nuacom API token

SAVE_FOLDER = ''                            # Ex 'C:\\jay\\example_folder'

FILTERS = {
    'type': 'outgoing',                     # Call direction filter: 'incoming', 'outgoing', or ''(both)
    'from_date': '2025-03-17 00:00:00',     # Start date/time of the call logs
    'to_date': '2025-06-17 23:59:59',       # End date/time of the call logs
    'billsec_above': '60',                  # Minimum billable seconds for call duration
    'billsec_below': '',                    # Maximum billable seconds for call duration
    'status': '',                           # Call status e.g. 'answered', 'missed', 'busy' 
    'from': '',                             # Caller phone number filter 
    'to': '',                               # Callee phone number filter 
    'call_id': '',                          # Specific call ID 
    'from_name': '',                        # Caller display name filter 
    'to_name': '',                          # Callee display name filter 
    'sort_by': 'call_date',                 # Field to sort results by
    'sort_dir': 'desc'                      # Sort direction: 'asc'=ascending or 'desc'=descending
}
