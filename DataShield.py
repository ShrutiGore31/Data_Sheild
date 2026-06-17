"""
--------------------------------------------------
Project Name : Data Shield System
Author       : Shruti Gore
Description  :
    Automated backup system that:
    1. Copies only new or modified files
    2. Creates periodic backups
    3. Generates ZIP archives
    4. Runs automatically using a scheduler
--------------------------------------------------
"""

# ==================================================
# Import Required Modules
# ==================================================

import sys
import os
import time
import schedule
import shutil
import hashlib
import zipfile


# ==================================================
# Create ZIP Archive
# ==================================================

def make_zip(folder):
    """
    Creates a ZIP archive of the backup folder.

    Parameters:
        folder (str): Folder to archive

    Returns:
        str: Generated ZIP file name
    """

    timestamp = time.strftime("%Y-%m-%d_%H-%M-%S")
    zip_name = folder + "_" + timestamp + ".zip"

    zobj = zipfile.ZipFile(zip_name, 'w', zipfile.ZIP_DEFLATED)

    for root, dirs, files in os.walk(folder):
        for file in files:
            full_path = os.path.join(root, file)
            relative = os.path.relpath(full_path, folder)

            zobj.write(full_path, relative)

    zobj.close()

    return zip_name


# ==================================================
# Calculate MD5 Hash
# ==================================================

def calculate_hash(path):
    """
    Calculates MD5 hash of a file.

    Parameters:
        path (str): File path

    Returns:
        str: MD5 hash value
    """

    hobj = hashlib.md5()

    with open(path, "rb") as fobj:
        while True:
            data = fobj.read(1024)

            if not data:
                break

            hobj.update(data)

    return hobj.hexdigest()


# ==================================================
# Backup New or Modified Files
# ==================================================

def BackupFiles(Source, Destination):
    """
    Copies only new or modified files from source
    directory to backup directory.

    Parameters:
        Source (str): Source directory
        Destination (str): Backup directory

    Returns:
        list: List of copied files
    """

    copied_files = []

    print("Creating backup folder...")

    os.makedirs(Destination, exist_ok=True)

    for root, dirs, files in os.walk(Source):

        for file in files:

            src_path = os.path.join(root, file)

            relative = os.path.relpath(src_path, Source)
            dest_path = os.path.join(Destination, relative)

            os.makedirs(os.path.dirname(dest_path), exist_ok=True)

            # Copy file if it is new or modified
            if (
                not os.path.exists(dest_path)
                or calculate_hash(src_path) != calculate_hash(dest_path)
            ):
                shutil.copy2(src_path, dest_path)
                copied_files.append(relative)

    return copied_files


# ==================================================
# Start Backup Process
# ==================================================

def DataShieldStart(Source="Data"):
    """
    Main backup process.
    """

    Border = "-" * 50

    BackupName = "ShrutiBackup"

    print(Border)
    print("Backup Process Started at :", time.ctime())
    print(Border)

    files = BackupFiles(Source, BackupName)

    zip_file = make_zip(BackupName)

    print(Border)
    print("Backup Completed Successfully")
    print("Files Copied :", len(files))
    print("ZIP File Created :", zip_file)
    print(Border)


# ==================================================
# Main Function
# ==================================================

def main():

    Border = "-" * 50

    print(Border)
    print("--------- Data Shield System ---------")
    print(Border)

    # ----------------------------------------------
    # Help Section
    # ----------------------------------------------

    if len(sys.argv) == 2:

        if sys.argv[1] in ("--h", "--H"):

            print("This script is used to:")
            print("1. Take automatic backups periodically")
            print("2. Backup only new and modified files")
            print("3. Create ZIP archives of backups")

        elif sys.argv[1] in ("--u", "--U"):

            print("Usage:")
            print("python DataShield.py TimeInterval SourceDirectory")
            print()
            print("TimeInterval     : Backup interval in minutes")
            print("SourceDirectory  : Folder to backup")

        else:

            print("Invalid option.")
            print("Use --h or --u for help.")

    # ----------------------------------------------
    # Project Execution
    # Example:
    # python DataShield.py 5 Data
    # ----------------------------------------------

    elif len(sys.argv) == 3:

        print("Inside Project Logic")
        print("Time Interval :", sys.argv[1], "minutes")
        print("Directory Name :", sys.argv[2])

        schedule.every(
            int(sys.argv[1])
        ).minutes.do(
            DataShieldStart,
            sys.argv[2]
        )

        print(Border)
        print("Data Shield System Started Successfully")
        print("Backup Interval :", sys.argv[1], "minutes")
        print("Press Ctrl + C to Stop")
        print(Border)

        while True:
            schedule.run_pending()
            time.sleep(1)

    else:

        print("Invalid number of arguments.")
        print("Use --h or --u for help.")

    print(Border)
    print("------ Thank You For Using Data Shield ------")
    print(Border)


# ==================================================
# Application Entry Point
# ==================================================

if __name__ == "__main__":
    main()
