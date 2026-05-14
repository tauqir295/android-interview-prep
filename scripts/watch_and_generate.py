from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler

from pathlib import Path
import subprocess
import sys
import time

# Directories to watch
WATCH_DIRECTORIES = [
    Path("data"),
    Path("templates"),
    Path("scripts")
]

# Allowed file extensions
WATCH_EXTENSIONS = (
    ".yaml",
    ".yml",
    ".j2",
    ".py"
)

# Prevent duplicate rapid executions
last_run = 0


class ProjectChangeHandler(FileSystemEventHandler):

    def process(self, event):

        global last_run

        # Ignore directories
        if event.is_directory:
            return

        file_path = event.src_path

        # Only process supported file types
        if not file_path.endswith(WATCH_EXTENSIONS):
            return

        # Ignore generated markdown updates
        if "docs/generated" in file_path:
            return

        # Debounce rapid save events
        current_time = time.time()

        if current_time - last_run < 1:
            return

        last_run = current_time

        print("\nDetected change:")
        print(file_path)

        print("\nGenerating markdown...\n")

        result = subprocess.run(
            [sys.executable, "scripts/generate_docs.py"],
            text=True
        )

        if result.returncode == 0:
            print("\nMarkdown generation completed successfully.\n")
        else:
            print("\nMarkdown generation failed.\n")

    def on_modified(self, event):
        self.process(event)

    def on_created(self, event):
        self.process(event)

    def on_moved(self, event):
        self.process(event)

    def on_deleted(self, event):
        self.process(event)


if __name__ == "__main__":

    print("Watching project files for changes...\n")

    event_handler = ProjectChangeHandler()

    observer = Observer()

    # Watch all configured directories
    for directory in WATCH_DIRECTORIES:

        observer.schedule(
            event_handler,
            str(directory),
            recursive=True
        )

        print(f"Watching: {directory}")

    observer.start()

    try:
        while True:
            time.sleep(1)

    except KeyboardInterrupt:
        print("\nStopping watcher...")

        observer.stop()

    observer.join()