from pathlib import Path
from enum import Enum

class FileName(Enum):
    TEMP_WAV = "temp.wav",
    EXTENSIONS = "extensions.json",
    CONNECTION = "connection.data",
    USER_DATA = "user.data"

class FileManager():
    def __init__(self):
        file_list = [
            "temp.wav",
            "jsons\\extensions.json",
            "data\\connection.data",
            "data\\user.data"
            ]
        self.path_lsit = list()
        for file in file_list:
            self.path_lsit.append(
                Path(__file__).resolve().parent.joinpath(file).__str__()
            )
    def debug(self):
        for p in self.path_lsit:
            print(p)

if __name__ == "__main__":
    fm = FileManager()
    fm.debug()