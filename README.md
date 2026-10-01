# Python File Organizer

A simple Python script that automatically organizes files into folders based on their file types.

## Features

- Organizes files into categories:
  - Images
  - Documents
  - PDFs
  - Videos
  - Audio
  - Archives
- Supports multiple file extensions.
- Handles uppercase and lowercase file extensions.
- Prevents duplicate filenames by automatically adding numbers such as `_1`, `_2`, etc.
- Allows the user to choose which folder to organize.
- Validates the folder path before organizing files.

## Built With

- Python
- pathlib

## How It Works

The program asks the user to enter a folder path.

It then checks each file's extension and moves the file into the appropriate category folder.

For example:

- `.jpg` → Images
- `.pdf` → PDFs
- `.mp4` → Videos
- `.mp3` → Audio
- `.zip` → Archives

If a file with the same name already exists, the program automatically creates a new filename instead of replacing the existing file.

Example:

photo.jpg  
photo_1.jpg  
photo_2.jpg

## How to Run

Run:

```bash
python file_organizer.py
