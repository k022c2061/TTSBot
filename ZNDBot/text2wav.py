import pyvcroid2
from user import User

def create_wav(text:str,u:User):
    file = "temp.wav"
    with pyvcroid2.VcRoid2() as vc:
        # Load language library
        lang_list = vc.listLanguages()
        if "standard" in lang_list:
            vc.loadLanguage("standard")
        elif 0 < len(lang_list):
            vc.loadLanguage(lang_list[0])
        else:
            raise Exception("No language library")
        
        # Load Voice
        voice_list = vc.listVoices()
        if 0 < len(voice_list):
            vc.loadVoice(voice_list[u.voice_charactor])
        else:
            raise Exception("No voice library")
        
        # Set parameters
        vc.param.volume = u.voice_volume
        vc.param.speed = u.voice_speed
        vc.param.pitch = u.voice_pitch
        vc.param.emphasis = u.voice_emhasis
        vc.param.pauseMiddle = 80
        vc.param.pauseLong = 100
        vc.param.pauseSentence = 200
        vc.param.masterVolume = 1.00

        speach,tts = vc.textToSpeech(text)

        with open(file,"wb") as f:
            f.write(speach)
            return file
    
    