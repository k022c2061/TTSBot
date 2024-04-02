import os
import pickle
from enum import IntEnum

#読み上げタイプクラス
class TTS_TYPE(IntEnum):
    ROID = 0,
    VOX = 1

class UserManager:
    def __init__(self,file_path):
        #ファイルパスの登録
        self.file_path = file_path
        #ユーザーデータの初期化
        self.user_data = dict()

        #ユーザーデータファイルのチェック
        #データファイルが存在する場合
        if os.path.getsize(self.file_path) != 0:
            self.load()
        #存在しないまたはデータがない場合
        else:
            pass

    #データの読み込み
    def load(self):
        try:
            with open(self.file_path,"rb") as f:
                self.user_data = pickle.load(f)
        except Exception as e:
            print(f"LoadUserdata Ex:{e}")

    #データの書き込み
    def write(self):
        if self.user_data:
            try:
                with open(self.file_path,"wb") as f:
                    pickle.dump(self.user_data,f)
            except Exception as e:
                print(f"LoadUserdata Ex:{e}")
        else:
            pass

    #データの新規追加
    def register(self,id :str):
        #データを一時保存
        buf = self.user_data
        #データが存在する場合はpass
        if id in buf.keys():
            pass
        else:
            try:
                #データの追加
                buf.setdefault(
                    id,
                    {
                    "id":id,
                    "type":0,
                    "speaker_roid":0,
                    "speaker_vox":0,
                    "speed":1.18,
                    "pitch":1.00,
                    "volume":1.00
                    }
                )
            except Exception as e:
                print(f"AppedUserdata Ex:{e}")
            else:
                self.user_data = buf

    def set_type(self,id : str,type : TTS_TYPE):
        #データを一時保存
        buf = self.user_data
        try:
            if id in buf.keys():
                print(id)
            else:
                raise Exception("ユーザーデータが存在しません")
        except Exception as e:
            print(f"fanc[set_type]Userdata Ex:{e}")

    def set_speaker(self,id : str,speaker :int):
        #データを一時保存
        buf = self.user_data
        try:
            if id in buf.keys():
                pass
            else:
                raise Exception("ユーザーデータが存在しません")
        except Exception as e:
            print(f"set_speaker:Userdata Ex:{e}")


if __name__ == "__main__":
    pass

"""
#データサンプル
    data = {
        "0":{
            "id":"0",
            "type":"roid",
            "speaker_roid":0,
            "speaker_vox":0,
            "speed":1.18,
            "pitch":1.00,
            "volume":1.00
        }
    }
"""
    