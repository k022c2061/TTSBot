import json

class User():
    id:str
    voice_volume:float
    voice_speed:float
    voice_pitch:float
    voice_emhasis:float
    voice_charactor:int
    
    def __init__(self,id:str):
        self.id = id
        self.voice_volume = 1.00
        self.voice_speed = 1.20
        self.voice_pitch = 1.00
        self.voice_emhasis = 1.00
        self.voice_charactor = 0

    def set_id(self,id:str):
        self.id = id

    def set_volume(self,volume:float):
        self.voice_volume = volume

    def set_speed(self,speed:float):
        self.voice_speed = speed
    
    def set_pitch(self,pitch:float):
        self.voice_pitch = pitch
    
    def set_emhasis(self,emhasis:float):
        self.voice_emhasis = emhasis
    
    def set_charactor(self,charactor:int):
        self.voice_charactor = charactor


class UserManager():
    def write_json(self,file,user_list:dict,type:int):
        tmp = dict()
        for n in user_list:
            if type == 1:
                tmp.setdefault(n,user_list[n].voice_charactor)
            else:
                tmp.setdefault(n,user_list[n].voice_charactor)
        json_str = json.dumps(tmp)
        with open(file,"w") as f:
            f.write(json_str)
                

    def load_user_ch(self,file):
        with open(file,"r") as f:
            data = json.load(f)
            return data

if __name__ == "__main__":
    file = "ch.json"
    n = UserManager()
    print(n.load_user_ch(file)) 