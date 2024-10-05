import easygui
import os

def select_file():
    file_path = easygui.fileopenbox()
    file_dir, file_name = os.path.split(file_path)
    return file_path, file_name
