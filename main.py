import os
import shutil

FOLDER_NAMES = ["PDFs", "Spreadsheets", "Text Files", "Images"]


def get_downloads_folder_path():
    """Returns the default downloads folder path for Windows or Linux"""
    if os.name == "nt":
        import winreg
        sub_key = r"SOFTWARE\Microsoft\Windows\CurrentVersion\Explorer\Shell Folders"
        downloads_guid = "{374DE290-123F-4565-9164-39C4925E467B}"
        with winreg.OpenKey(winreg.HKEY_CURRENT_USER, sub_key) as key:
            location = winreg.QueryValueEx(key, downloads_guid)[0]
        return location
    else:
        return os.path.join(os.path.expanduser("~"), "Downloads")


def sort_files_into_directories():
    """Sorts files into directories by their extension and creates directories if they don't exist"""

    downloads_folder_path = get_downloads_folder_path()

    for i in range(0, len(FOLDER_NAMES)):
        if not os.path.exists(os.path.join(downloads_folder_path, FOLDER_NAMES[i])):
            os.mkdir(os.path.join(downloads_folder_path, FOLDER_NAMES[i]))

    files_list = os.listdir(downloads_folder_path)
    for file_name in files_list:
        if file_name.endswith(".txt"):
            text_files_path = os.path.join(downloads_folder_path, "Text Files")
            shutil.move(os.path.join(downloads_folder_path, file_name), os.path.join(text_files_path, file_name))

        elif file_name.endswith(".xls") or file_name.endswith(".xlsx"):
            spreadsheets_files_path = os.path.join(downloads_folder_path, "Spreadsheets")
            shutil.move(os.path.join(downloads_folder_path, file_name), os.path.join(spreadsheets_files_path, file_name))

        elif file_name.endswith(".png") or file_name.endswith(".jpeg") or file_name.endswith(".gif"):
            image_files_path = os.path.join(downloads_folder_path, "Images")
            shutil.move(os.path.join(downloads_folder_path, file_name), os.path.join(image_files_path, file_name))

        elif file_name.endswith(".pdf"):
            pdf_files_path = os.path.join(downloads_folder_path, "PDFs")
            shutil.move(os.path.join(downloads_folder_path, file_name), os.path.join(pdf_files_path, file_name))


sort_files_into_directories()
