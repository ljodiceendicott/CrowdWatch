from oauth2client.service_account import ServiceAccountCredentials
import gspread
import json
scopes = [
'https://www.googleapis.com/auth/spreadsheets',
'https://www.googleapis.com/auth/drive'
]
credentials = ServiceAccountCredentials.from_json_keyfile_name("key.json", scopes) #access the json key you downloaded earlier 
file = gspread.authorize(credentials) # authenticate the JSON key with gspread
sheet = file.open("blank")  #open sheet
cell = sheet.sheet1.cell('1','1')
# sheet = sheet.sheet_name  #replace sheet_name with the name that corresponds to yours, e.g, it can be sheet1

# This is the literal cells
print(cell)
# prints the value found in the cell
print(cell.value) 

allcells = sheet.sheet1.batch_get(['A1:B5'])
print(allcells)

# Updateing a value that is in the sheet
sheet.sheet1.update('A1:C3', [["VALUE","Value"]])


# for cell in allcells:
#     print(cell.value)