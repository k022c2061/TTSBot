from pathlib import Path
import pickle
#import os

class connection_wrap():
    def __init__(self):
        self.file = Path(__file__).resolve().parent.parent.joinpath("data\\connection.data")
        self.data = list()
        
    def add_connection(self,connection_id :str,tts_channel : str):
        try:
            self.data.append(
                {
                    'connection_id':connection_id,
                    'tts_channel' : tts_channel
                 }
            )
            self.dump()
        except Exception as e :
            print(f"connection_wrap.add_connection Exption:{e}")
        
    def load(self):
        try:
            with open(self.file,"rb") as f:
                data = pickle.load(f)
                if type(data) != list():
                    raise Exception()
                else:
                    self.data = data
        except Exception as e:
            print(f"connection_wrap.load Exption:{e}")

    
    def dump(self,data : list):
        try:
            with open(self.file,"wb") as f:
                pickle.dump(data,f)
        except Exception as e:
            print(f"connection_wrap.dump Exption:{e}")
        
if __name__ == "__main__":
    cw = connection_wrap()
    temp = [
                {
                    "connection_id":"1",
                    "tts_channel" : "0"                        
                }
            ]
    cw.dump(temp)
    cw.load()
    print(cw.data)
    