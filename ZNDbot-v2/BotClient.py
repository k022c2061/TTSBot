import discord
from discord.ext import commands
from managers.users import UserManager
from managers.extensions import ExtensionManager
from handlers.path import FilePathHandler

#BotObject
class ZNDbot(commands.Bot):
    def __init__(self,pfx:str,intents:discord.Intents):
        #init default
        super().__init__(
            command_prefix=commands.when_mentioned_or(pfx),
            intents=intents,
            help_command=None
        )
        #ファイルハンドラ
        self.file_handler = FilePathHandler("ZNDbot")
        #ファイル位置を取得
        user_data_path = self.file_handler.get_absolute_path("data/users.data")
        extension_json_path = self.file_handler.get_absolute_path("jsons/extensions.json")
        #ユーザーデータ管理
        self.user_manager = UserManager(user_data_path)
        #cogの管理
        self.extensions_manager = ExtensionManager(extension_json_path)
        
    async def boot(self,extensions):
        for cogs in extensions["cogs"]:
            await self.load_extension(cogs)

    async def setup_hook(self):
        try:
            await self.boot(self.extensions_manager.extensions_data)
            synced = await self.tree.sync()
            print(f"{len(synced)} commands synced!")
        except Exception as e:
            print(f"CommandSyncExeption:{e}")

    async def on_ready(self):
        print(f"Login:{self.user}")
        await self.change_presence(
            activity=discord.Activity(
                name="読み上げ",
                type=discord.ActivityType.listening,
            )
        )

if __name__ == "__main__":
    pass