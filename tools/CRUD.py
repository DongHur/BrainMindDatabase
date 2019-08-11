import numpy as np
from googleapiclient.discovery import build

class CRUD_obj():
    def __init__(self, creds, sheet_id):
        self.creds = creds
        self.service = build('sheets', 'v4', credentials=self.creds)
        self.sheet = self.service.spreadsheets()
        self.SHEET_ID = sheet_id
    def create(self):
        pass
    def read(self, ranges, majorDimension='ROWS'):
        # send request to google to get data
        result = self.sheet.values().batchGet(spreadsheetId=self.SHEET_ID, ranges=ranges, 
            majorDimension=majorDimension).execute()
        valueRanges = result.get('valueRanges', [])
        return valueRanges
    def update(self):
        pass
    def delete(self):
        pass