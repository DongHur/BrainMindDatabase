from __future__ import print_function
import pickle
import os.path
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request

# If modifying these scopes, delete the file token.pickle.
SCOPES = ['https://www.googleapis.com/auth/spreadsheets.readonly']

def main():
	"""Shows basic usage of the Sheets API.
	Prints values from a sample spreadsheet.
	"""
	creds = None
	# The file token.pickle stores the user's access and refresh tokens, and is
	# created automatically when the authorization flow completes for the first
	# time.
	if os.path.exists('token.pickle'):
	    with open('token.pickle', 'rb') as token:
	        creds = pickle.load(token)
	        print("Already Logged In")
	# If there are no (valid) credentials available, let the user log in.
	if not creds or not creds.valid:
	    if creds and creds.expired and creds.refresh_token:
	        creds.refresh(Request())
	    else:
	        flow = InstalledAppFlow.from_client_secrets_file(
	            'credentials.json', SCOPES)
	        creds = flow.run_local_server()
	    # Save the credentials for the next run
	    print("Creating Credential")
	    with open('token.pickle', 'wb') as token:
	        pickle.dump(creds, token)

if __name__ == '__main__':
    main()