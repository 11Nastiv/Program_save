from watchdog.observers import Observer
import os
import time 
from watchdog.events import FileSystemEventHandler

class EventHandler(FileSystemEventHandler):
    def on_modified(self, event):
        for filename in os.listdir(folder_track):
            extension = filename.split(".")
            if len(extension) > 1 and (extension[1].lower() == "jpg" or extension[1].lower() == "png" or extension[1].lower() == "pdf"):
                file = folder_track + "/" + filename
                new_path = folder_dest + "/" + filename
                os.rename(file, new_path)

folder_track = 'C:/Users/Nastiv/Downloads'
folder_dest = 'C:/Users/Nastiv/Desktop/Photos'

event_handler = EventHandler()
observer = Observer()
observer.schedule(event_handler, folder_track, recursive=True)
observer.start()

try:
    while(True):
        time.sleep(10)
except KeyboardInterrupt:
    observer.stop()
observer.join()
