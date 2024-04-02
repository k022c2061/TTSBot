import pyvcroid2
from pathlib import Path
import json
import urllib.request

file = Path(__file__).resolve().parent.joinpath("temp.wav")

#ファイル生成->接続->再生
#FilePath を戻り値に返す関数

def CREATE_WAV_roid(text:str,user_setting:dict):
    with (pyvcroid2.VcRoid2() as vc,open(file,"wb") as f):
        # Load language library
        lang_list = vc.listLanguages()
        if "standard" in lang_list:
            vc.loadLanguage("standard")
        elif 0 < len(lang_list):
            vc.loadLanguage(lang_list[0])
        else:
            raise Exception("No language library")
        print(lang_list)
    
        # Load Voice
        voice_list = vc.listVoices()
        # Select speaker
        speaker = voice_list[user_setting['speaker_roid']]
        if 0 < len(voice_list):
            #set speaker
            if speaker =='akane_west_emo_44':
                vc.loadLanguage(lang_list[1])
            vc.loadVoice(speaker)
        else:
            raise Exception("No voice library")

        # Set parameters
        vc.param.volume = user_setting['volume']
        vc.param.speed = user_setting['speed']
        vc.param.pitch = user_setting['pitch']
        vc.param.emphasis = 0.893
        vc.param.pauseMiddle = 80
        vc.param.pauseLong = 100
        vc.param.pauseSentence = 200
        vc.param.masterVolume = 1.00

        text += "。"
        tts,event = vc.textToSpeech(text)
        f.write(tts)
        
        return file.__str__()
    
def CREATE_WAV_vox(text : str,speaker : int):
    api = "https://api.tts.quest/v3/voicevox/synthesis"
    file = Path(__file__).absolute().parent.joinpath("temp.wav")
    try : 
        with urllib.request.urlopen(f"{api}?text={text}&speaker={speaker}") as res:
            body = json.load(res)
            print(body["wavDownloadUrl"])
            s,h = urllib.request.urlretrieve(body["wavDownloadUrl"],file)
            print(s)
            print(h)
    except Exception as e:
        print(e)
    else:
        return file
    finally :
        pass

if __name__ == "__main__":
    CREATE_WAV_roid("しろからきたで",0)
