# Data Shield System

## Overview

Data Shield System is a Python-based automation tool that performs periodic backups of files and folders. The system detects new or modified files using MD5 hashing, copies them to a backup directory, and creates ZIP archives for secure storage.

This project demonstrates Python automation, file handling, scheduling, hashing, compression, and command-line argument processing.

---

## Features

* Automated scheduled backups
* Copies only new and modified files
* MD5 hash-based file comparison
* ZIP archive generation
* Preserves original folder structure
* Command-line interface support
* Continuous background execution using a scheduler

---

## Technologies Used

* Python
* Schedule Library
* OS Module
* Hashlib Module
* Shutil Module
* ZipFile Module

---

## Installation

Clone the repository:

```bash
git clone https://github.com/your-username/Data-Shield-System.git
cd Data-Shield-System
```

Install required dependency:

```bash
pip install schedule
```

---

## Usage

### Display Help

```bash
python DataShield.py --h
```

### Display Usage Information

```bash
python DataShield.py --u
```

### Run Automatic Backup

```bash
python DataShield.py 5 Data
```

Where:

* `5` = Backup interval in minutes
* `Data` = Source directory to be backed up

---

## Example Output

```text
--------------------------------------------------
Backup Process Started at :
Tue Jun 16 20:30:15 2026
--------------------------------------------------
Backup Completed Successfully
Files Copied : 5
ZIP File Created : ShrutiBackup_2026-06-16_20-30-15.zip
--------------------------------------------------
```

---

## Project Structure

```text
Data-Shield-System/
│
├── DataShield.py
├── README.md
├── requirements.txt
├── .gitignore
└── LICENSE
```

---

## Working Process

1. User specifies a backup interval and source directory.
2. The scheduler runs the backup process periodically.
3. The system compares file hashes to detect changes.
4. New or modified files are copied to the backup folder.
5. A ZIP archive of the backup folder is created.
6. The process repeats automatically at the specified interval.

---

## Future Enhancements

* Email notifications after backup completion
* Cloud storage integration
* Backup logs generation
* GUI version using Tkinter
* Multi-directory backup support

---

## Author

**Shruti Gore**

Python Automation Project

