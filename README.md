# This is a script that sorts the files in your download folder to specific folders

## These specific folders can be changed within the code and personalized to your liking by updating these code segments
First add or change the FOLDER_NAMES list to your liking:
'''
  FOLDER_NAMES = ["PDFs", "Spreadsheets", "Text Files", "Images"]
'''
Then add another elif for the file with the exstension you want: 

'''
elif file_name.endswith(".pdf"):
      pdf_files_path = os.path.join(downloads_folder_path, "PDFs")
      shutil.move(os.path.join(downloads_folder_path, file_name), os.path.join(pdf_files_path, file_name))
'''

Run the script and your Downloads folder will thank you.
