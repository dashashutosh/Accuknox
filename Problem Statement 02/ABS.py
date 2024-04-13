import shutil
import os

# Specify the directory to be backed up
source_directory = input("Enter the path of the source directory: ")

# Specify the destination directory on the remote server or cloud storage
destination_directory = input("Enter the path of the destination directory: ")

def backup_directory():
    try:
        # Perform the backup operation
        files = os.listdir(source_directory)
        for file_name in files:
            source_file = os.path.join(source_directory, file_name)
            destination_file = os.path.join(destination_directory, file_name)
            shutil.copy(source_file, destination_file)
        print("Backup successful!")
    except Exception as e:
        print(f"Backup failed: {e}")

if __name__ == "__main__":
    backup_directory()
