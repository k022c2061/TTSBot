from discord.ext import commands
import pickle
import re
import os

class reconnectCog(commands.Cog):
    def __init__(self,bot : commands.Bot):
        super().__init__()
        self.bot = bot

    @commands.Cog.listener("on_ready")
    async def on_ready(self):
        pass


    #再接続した際にコネクションの状態を確認して、齟齬がある場合には修正するイベントリスナ
    
        

async def setup(bot : commands.Bot):
    await bot.add_cog(reconnectCog(bot))