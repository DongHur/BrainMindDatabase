from googleapiclient.discovery import build
import os.path
import pickle

# The ID and range of a sample spreadsheet.
SAMPLE_SPREADSHEET_ID = '1_hyrK6CMgeH4DXGF_boLJP27hdPfGo9tTt9PjFo-rmA'
SAMPLE_RANGE_NAME = "'Master List (unscrubbed)'!3:6"

def init_sheet():
	sheet = None
	if os.path.exists('token.pickle'):
		creds = None
		with open('token.pickle', 'rb') as token:
			creds = pickle.load(token)
		service = build('sheets', 'v4', credentials=creds)
		# Call the Sheets API
		sheet = service.spreadsheets()
		print("Authenticated.")
	else:
		print("Did Not Login.")
	return sheet

def get_data(sheet):
	result = sheet.values().get(spreadsheetId=SAMPLE_SPREADSHEET_ID, range=SAMPLE_RANGE_NAME).execute()
	data = result.get('values', [])
	return data

def main():
	sheet = init_sheet()
	data = get_data(sheet)
	

	if not data:
		print('No data found.')
	else:
		for row in data:
			# Print columns A and E, which correspond to indices 0 and 4.
			print('%s, %s' % (row[0], row[4]))

if __name__ == '__main__':
	main()