#!/usr/bin/env python3

import miniaudio
from pathlib import Path







def main():


    base_path = Path.cwd()

    print("Welcome to Velvet")

    #song = Path(input("Whats the path of the song you want to play:\n% "))


    song_name = input("What song do you want to play:\n> ")
    song = Path(str(base_path) + '/' + song_name)
    print(song)


    song_info = miniaudio.get_file_info(song)

    print(f"Playing: {song_info.nchannels} channels, {song_info.sample_rate} Hz, {song_info.duration:.1f}s")


    stream = miniaudio.stream_file(song)

    with miniaudio.PlaybackDevice() as device:
        device.start(stream)
        input("Playing... press Enter to stop")



main()
