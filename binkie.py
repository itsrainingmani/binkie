import os
import sys
import time

import sounddevice as sd
import soundfile as sf
from random import choice

CHUNK = 1024


def play_sound(path_to_sound_file):
    data, fs = sf.read(path_to_sound_file)
    sd.play(data, fs)
    sd.wait()


def check_zoom_meeting():
    zoom_procs = "ps aux | grep 'CptHost.app/Contents/MacOS/CptHost'"
    list_procs = os.popen(zoom_procs, "r")
    data = [line for line in list_procs.readlines() if "grep" not in line]
    return len(data) != 0


def load_sounds():
    relaxing_sound_library = []
    dir = os.listdir("./calmsounds")
    return dir


if __name__ == "__main__":
    library = load_sounds()
    try:
        while True:
            in_zoom = check_zoom_meeting()
            if in_zoom:
                print("Zoomies fr ong")
                sound = choice(library)
                play_sound(f"./calmsounds/{sound}")
            else:
                print("unburdened. unzoomed")
            time.sleep(5)
    except KeyboardInterrupt:
        sys.exit(0)
