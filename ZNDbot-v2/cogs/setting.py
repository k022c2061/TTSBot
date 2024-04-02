from discord.ext import commands
from discord import app_commands,Interaction

@app_commands.guild_only()
class SettingCog(commands.GroupCog,group_name="setting"):
    def __init__(self,bot : commands.Bot):
        super().__init__()
        self.bot = bot

"""
    @app_commands.command(name="add-word",description="単語を辞書に追加します")
    @app_commands.rename(word="単語")
    @app_commands.rename(yomi="読み方")
    @app_commands.describe(word="登録単語")
    @app_commands.describe(yomi="ひらがなで入力")
    async def add_Word(self,ctx : Interaction,word : str,yomi : str):
        try:
            pass
        except Exception as e:
            print(f"setting add_word Exception:{e}")
        finally:
            pass

    @app_commands.command(name="del-word",description="単語を辞書から削除します")
    async def delete_Word(self,ctx : Interaction):
        try:
            pass
        except Exception as e:
            print(f"setting del_word Exception:{e}")
        finally:
            pass

    @app_commands.command(name="a",description="aaaa")
    async def add_phrease(self,ctx : Interaction):
        pass
"""
        
async def setup(bot : commands.Bot):
    await bot.add_cog(SettingCog(bot))
    