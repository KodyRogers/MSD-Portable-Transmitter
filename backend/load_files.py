import os
from mutagen import File
from datetime import datetime

def load_files():
    files = []

    for file in os.listdir("files/audio"):
        if file.endswith(".mp3") or file.endswith(".wav"):
            filepath = os.path.join("files/audio", file)

            audio = File(filepath)
            stats = os.stat(filepath)
            if audio is not None:
                files.append({
                    "filename": file,
                    "filepath": filepath,
                    "duration": audio.info.length,
                    "modified": datetime.fromtimestamp(stats.st_mtime)
                })
            else:
                print(f"Unsupported file format: {file}")
    return files