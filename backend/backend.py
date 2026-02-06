import serial
import time

from datetime import datetime
from gtts import gTTS

SERIAL_PORT = "/dev/serial0"
BAUDRATE = 9600
BUF_SIZE = 256

AUDIO_DIR = "./files/audio/"
GPS_DIR = "./files/gps/"

def init_serial():
    ser = serial.Serial(SERIAL_PORT, BAUDRATE, timeout=1)
    time.sleep(2)  # Wait for the serial connection to initialize
    return ser

# TODO: Implement GPS data retrieval
def get_gps_data():
    temp = {"lat": "0.0", "lon": "0.0"}
    return temp

# TODO: Implement audio playback
def play_audio(file_path):
    pass

# TODO: 
def create_audio(files, iterations, start_delay, delay_between):
    pass

# TODO
def save_data():
    
    timestamp = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
    gps_data = get_gps_data()
    with open(GPS_DIR + f"{timestamp}.txt", "w") as f:
        f.write(f"Latitude: {gps_data['lat']}\n")
        f.write(f"Longitude: {gps_data['lon']}\n")
    
    
    tts = gTTS("Hello, this is a test." + timestamp, lang="en")
    tts.save(AUDIO_DIR + f"{timestamp}.mp3")

    print(timestamp)

def start_logs():
    #TODO
    pass

def main():
    save_data()

if __name__ == "__main__":
    main()
    