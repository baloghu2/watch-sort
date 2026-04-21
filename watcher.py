import os
import time
import subprocess
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler

class NewFileHandler(FileSystemEventHandler):
    def on_created(self, event):
        # Check if the event is a file and not a directory
        if not event.is_directory:
            print(f"New file detected: {event.src_path}")
            dir_path = os.path.dirname(event.src_path)
            # Run local sort.py on the containing directory
            sort_script = os.path.join(os.path.dirname(__file__), 'sort', 'sort.py')
            subprocess.run(['python', sort_script, dir_path])

if __name__ == "__main__":
    # Multiple paths to watch (add your folders here)
    paths = [
        "C:/Users/jamie/Desktop/Incoming",  # testing folder
        "C:/Users/jamie/AppData/Roaming/nicotine/downloads", # Watching the Nicotine+ downloads folder
        "C:/Users/jamie/Downloads", # Watching the default Downloads folder
        "C:/Users/jamie/Desktop",  # Watching the Desktop as well
    ]

    event_handler = NewFileHandler()
    observer = Observer()
    for path in paths:
        if os.path.exists(path):
            observer.schedule(event_handler, path, recursive=False)
            print(f"Watching: {path}")
        else:
            print(f"Path not found, skipping: {path}")
    
    observer.start()
    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        observer.stop()
    observer.join()
