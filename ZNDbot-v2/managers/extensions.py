import json
import pickle
import os
from pathlib import Path

connection_file = Path(__file__).resolve().parent.joinpath("jsons\\connection\\connection.data")

def load_connection_data()->dict():
    with open(connection_file,"rb") as f:
        data = pickle.load(f)
        if type(data) != dict:  # noqa: E721
            raise Exception()
        else:
            return data

class ExtensionManager:
    def __init__(self,file_path):
        #パスの登録
        self.file_path = file_path
        #データの初期化
        self.extensions_data = dict()

        #データファイルのチェック
        #データファイルが存在する場合
        if os.path.getsize(self.file_path) != 0:
            self.load()
        #存在しないまたはデータがない場合
        else:
            pass

    def load(self):
        with open(self.file_path,"r") as f:
            self.extensions_data = json.load(f)



if __name__ == "__main__":
        data = [
            {
                "connection_id" : "0",
                "tts_channel" : "0"
            },
        ]