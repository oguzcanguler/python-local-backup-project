import tkinter as tk
from tkinter import filedialog
import shutil
import time


if __name__ == '__main__':
    root = tk.Tk()
    root.withdraw()
    print("Select file to backup")
    file_path = filedialog.askopenfilename()  # select input file location for backup

    print("Selected file path is : " + file_path)
    x = file_path.split("/")
    backup_filename = x[-1].split(".")
    file_extension = "." + backup_filename[1]
    backup_filename = backup_filename[0] + "_Backup"

    print("Select folder to copy backup file")
    folder_path = filedialog.askdirectory()  # select target folder location
    print("Selected folder to copy : " + folder_path)
    target = folder_path + "/" + backup_filename
    time_delay = int(input("How frequently you want to backup (second) ?"))
    backup_count = 1
    while True:
        print(target + str(backup_count) + file_extension)
        shutil.copyfile(file_path, target + str(backup_count) + file_extension)
        backup_count += 1
        print("File is backed up. Folder : " + folder_path)
        time.sleep(time_delay)  # Delay for 1 minute (60 seconds).
