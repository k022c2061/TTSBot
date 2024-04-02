from BotClient import ZNDbot
from discord import Intents
import os


if __name__ == "__main__":
 
    intents = Intents.default()
    intents.message_content = True
    intents.voice_states = True
    bot = ZNDbot("z!",intents)

    token = os.getenv("DISCORD_TOKEN_ZNDTalk")
    

    bot.run(token)