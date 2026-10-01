from pathlib import Path
folder_path = input("Enter the folder path you want to organize: ")
folder = Path(folder_path)
if not folder.exists() or not folder.is_dir():
    print("Invalid folder path.")
    raise SystemExit

categories = {
    "Images": [".jpg", ".jpeg", ".png", ".webp"],
    "Documents": [".txt", ".docx", ".doc"],
    "PDFs": [".pdf"],
    "Videos": [".mp4", ".mov", ".avi"],
    "Audio": [".mp3", ".wav", ".m4a"],
    "Archives": [".zip", ".rar", ".7z"]
}
def move_file(file, destination_folder):
    destination = destination_folder / file.name
    if destination.exists():
        counter = 1
        while destination.exists():
            destination = destination_folder / f"{file.stem}_{counter}{file.suffix}"
            counter += 1
    file.rename(destination)

for file in folder.iterdir():
    if not file.is_file():
        continue

    extension = file.suffix.lower()

    for category, extensions in categories.items():
        if extension in extensions:
            destination_folder = folder / category
            destination_folder.mkdir(exist_ok=True)

            move_file(file, destination_folder)
            print(file.name, "→", category)
            break
    else:
        print(file.name, "→ Unknown file type")
print("\nOrganization complete!")