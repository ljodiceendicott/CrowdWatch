import pydrive
from pydrive.auth import GoogleAuth
from pydrive.drive import GoogleDrive
from oauth2client.service_account import ServiceAccountCredentials


gauth = GoogleAuth()
gauth.LocalWebserverAuth() # client_secrets.json need to be in the same directory as the script
drive = GoogleDrive(gauth)


# Auto-iterate through all files that matches this query
file_list = drive.ListFile({'q': "'root' in parents and trashed=false"}).GetList()
for file1 in file_list:
    print('title: %s, id: %s' % (file1['title'], file1['id']))
print(file_list[1])

# View all folders and file in your Google Drive
# fileList = drive.ListFile({'q': "'root' in parents and trashed=false"}).GetList()
# for file in fileList:
#   print('Title: %s, ID: %s' % (file['title'], file['id']))
#   # Get the folder ID that you want
#   if(file['title'] == "To Share"):
#       fileID = file['id']

# file1 = drive.CreateFile({"mimeType": "text/csv", "parents": [{"kind": "drive#fileLink", "id": fileID}]})
# file1.SetContentFile("small_file.csv")
# file1.Upload() # Upload the file.
# print('Created file %s with mimeType %s' % (file1['title'], file1['mimeType']))   