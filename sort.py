import os
import shutil
import sys

def choose_directory():
    default_path = os.path.join(os.path.expanduser("~"), "Desktop")
    while True:
        path = input(f"Enter directory to sort (or press Enter for {default_path}/): ").strip()
        if not path:
            path = default_path
        if os.path.isdir(path):
            return os.path.abspath(path)
        else:
            print(f"Directory does not exist: {path}. Please try again.")

def main(current):
    os.chdir(current)
    print("directory being sorted: " + current)

    # Create base directory path (current folder itself)
    base_dir = current

    # List of folders to create
    folders = ['images', 'documents', 'audio', 'video', 'apps', 'codes', 'archives', 'books', 'unsorted', 'sheets']

    # Folders will be created on demand when files are found

    files = os.listdir(current)

    images = [".jpeg", ".png", ".jpg", ".gif", ".heic", ".bmp", ".tiff", ".svg"]
    documents = [".doc", ".txt", ".pdf", ".docx", ".rtf"]
    sheets = [".xlsx", ".xls", ".csv"]
    video = [".mp4", ".mkv", ".avi", ".mov", ".wmv"]
    audio = [".mp3", ".wav", ".m4a", ".flac", ".aac"]
    apps = [".exe", ".lnk"]
    archives = [".zip", ".rar", ".7z"]
    books = [".epub", ".mobi"]
    installers = [".exe", ".msi"]

    print("Sorting the files...")

    # Files to skip (system files, hidden files, etc.)
    skip_files = ['desktop.ini', 'thumbs.db', '.ds_store', '.py', '.git', 
                  '.gitignore', '.vscode', '__pycache__', '.idea', 
                  '.vs', '.svn', '.hg', '.tox', '.nox', '.pytest_cache', 
                  '.mypy_cache', '.ruff_cache', '.eggs', 'node_modules', 
                  'venv', 'env', 'virtualenv', 'dist', 'build', 'egg-info', 
                  '.part', '.svg.part', '.lnk', '.url', '.ini', '.log', '.bak', '.tmp',
                  '.temp']

    # Separate skip files into filenames and extensions
    skip_filenames = [item for item in skip_files if not item.startswith('.')]
    skip_extensions = [item for item in skip_files if item.startswith('.')]

    for file in files:
        if os.path.isdir(os.path.join(current, file)):
            continue
        if file.lower() in skip_filenames or any(file.lower().endswith(ext) for ext in skip_extensions):
            continue
        dest = ""
        for ex in images:
            if file.lower().endswith(ex):
                dest = os.path.join(base_dir, 'images'); break
        for ex in documents:
            if dest == "" and file.lower().endswith(ex):
                dest = os.path.join(base_dir, 'documents'); break
        for ex in sheets:
            if dest == "" and file.lower().endswith(ex):
                dest = os.path.join(base_dir, 'sheets'); break
        for ex in video:
            if dest == "" and file.lower().endswith(ex):
                dest = os.path.join(base_dir, 'video'); break
        for ex in audio:
            if dest == "" and file.lower().endswith(ex):
                dest = os.path.join(base_dir, 'audio'); break
        for ex in apps:
            if dest == "" and file.lower().endswith(ex):
                dest = os.path.join(base_dir, 'apps'); break
        for ex in archives:
            if dest == "" and file.lower().endswith(ex):
                dest = os.path.join(base_dir, 'archives'); break
        for ex in books:
            if dest == "" and file.lower().endswith(ex):
                dest = os.path.join(base_dir, 'books'); break
        for ex in installers:
            if dest == "" and file.lower().endswith(ex):
                dest = os.path.join(base_dir, 'installers'); break 

        # If file extension does not match any known category, move to 'unsorted' folder
        if dest == "":
            dest = os.path.join(base_dir, 'unsorted')
            os.makedirs(dest, exist_ok=True)
            shutil.move(file, os.path.join(dest, file))
        else:
            os.makedirs(dest, exist_ok=True)
            shutil.move(file, os.path.join(dest, file))

    print("Sorting Completed...")

# Non-interactive mode if directory provided as arg (must come after def main)
if len(sys.argv) > 1:
    current = os.path.abspath(sys.argv[1])
    if os.path.isdir(current):
        print(f"Auto-sorting directory: {current}")
        main(current)
        sys.exit(0)
    else:
        print(f"Error: Directory does not exist: {current}")
        sys.exit(1)

# Interactive mode
while True:
    current = choose_directory()
    main(current)
    response = input("Do you want to sort another folder? (y/n): ").strip().lower()
    if response != 'y':
        break
