import datetime
import os
import random
import discord
from discord import app_commands
from text2wav import create_wav
from user import User,UserManager
from pathlib import Path
import asyncio
import re

class ZNDBot(discord.Client):
    def __init__(self,intent:discord.Intents):
        super().__init__(intents=intent)
        self.tree = app_commands.CommandTree(self)
        self.message_channel_list = list()
        self.user_list = dict()
        self.user_list.setdefault("0",User("0"))
        self.um = UserManager()

        self.file = Path(__file__).resolve().parent.joinpath("ch.json")

        if os.path.getsize(self.file) == 0:
             self.um.write_json(file=self.file,user_list=self.user_list,type=1)
        else :
            self.load_ch()


        @self.tree.command(name="zjoin",description="ボイスチャンネルに接続します")
        @app_commands.guild_only()
        async def join(ctx:discord.Interaction):
            await ctx.response.defer(thinking=True)
            embed = self.mkembed(ctx.user)
            if ctx.user.voice is None:
                embed.color = 0xdc143c
                embed.add_field(name="",value=f"**{ctx.user.mention}はボイスチャンネルに接続されていません**",inline=True)
            elif ctx.guild.voice_client is not None and ctx.guild.voice_client.is_connected():
                embed.color = 0xdc143c
                embed.add_field(name="",value=f"**{self.user.name}は既にボイスチャンネルに接続されています**",inline=True)
            else:
                embed.add_field(name="接続しました",value=f"{ctx.user.voice.channel.jump_url}に接続しました",inline=True)
                if not ctx.user.id.__str__() in self.user_list.keys():
                    source = discord.FFmpegPCMAudio(create_wav("接続しました",self.user_list["0"]))
                else:
                    source = discord.FFmpegPCMAudio(create_wav("接続しました",self.user_list[ctx.user.id.__str__()]))
                voice_client_data = await ctx.user.voice.channel.connect()
                voice_client_data.play(source)
                self.message_channel_list.append(ctx.channel.id)
            await ctx.followup.send(embed=embed)

        @self.tree.command(name="zdisconnect",description="ボイスチャンネルから切断します")
        async def disconnect(ctx:discord.Interaction):
            embed = self.mkembed(ctx.user)
            if ctx.guild.voice_client is None:
                embed.color = 0xdc143c
                embed.add_field(name="",value=f"**{ctx.user.mention} ボイスチャンネルに接続していません**",inline=True)
            else:
                if not ctx.channel_id in self.message_channel_list:
                    embed.color = 0xdc143c
                    embed.add_field(name="",value="/joinを使用したチャンネルで使用してください",inline=True)
                else:
                    await ctx.guild.voice_client.disconnect()
                    self.message_channel_list.pop(self.message_channel_list.index(ctx.channel_id))
                    embed.add_field(name="切断しました",value="",inline=True)
            await ctx.response.send_message(embed=embed)

        @self.tree.command(name="zsetvoice",description="話者を設定します。")
        @app_commands.guild_only()
        @app_commands.describe(ch="キャラクター")
        @app_commands.rename(ch="話者")
        @app_commands.choices(
            ch=[
                app_commands.Choice(name="琴葉茜",value=0),
                app_commands.Choice(name="琴葉葵",value=2),
                app_commands.Choice(name="紲星あかり",value=1),
                app_commands.Choice(name="東北ずん子",value=3),
            ]
        )
        async def setvoice(ctx:discord.Interaction,ch:int):
            chara_dict ={0:"琴葉茜",1:"紲星あかり",2:"琴葉葵",3:"東北ずん子"}
            embed = self.mkembed(ctx.user)
            if not ctx.user.id in self.user_list.keys():
                self.user_list.setdefault(ctx.user.id.__str__(),User(ctx.user.id.__str__()))
            if ch == self.user_list[ctx.user.id.__str__()].voice_charactor:
                embed.color = 0xdc143c
                embed.add_field(name="",value=f"**{ctx.user.mention}**",inline=False)
                embed.add_field(name="",value="**設定されている話者は同じです**",inline=True)
                await ctx.response.send_message(embed=embed)
                return
            embed.add_field(name="",value=f"{ctx.user.mention}の話者を変更しました",inline=False)
            embed.add_field(name="",value=f"**{chara_dict[self.user_list[ctx.user.id.__str__()].voice_charactor]}**",inline=False)
            embed.add_field(name="",value="**↓↓↓↓↓**",inline=False)
            self.user_list[ctx.user.id.__str__()].set_charactor(ch)
            embed.add_field(name="",value=f"**{chara_dict[self.user_list[ctx.user.id.__str__()].voice_charactor]}**",inline=False)
            self.um.write_json(self.file,self.user_list,1)
            if ch == 3:
                self.user_list[ctx.user.id.__str__()].set_pitch(0.83)
            else:
                self.user_list[ctx.user.id.__str__()].set_pitch(1)
            await ctx.response.send_message(embed=embed)


    def mkembed(self,user:discord.User | discord.Member) -> discord.Embed:
        '''
        Embedのテンプレートを作成します

        Return
        -------
        discord.Embed object
        '''
        embed = discord.Embed(
            color=0x90ee90
        )
        dt_time = datetime.datetime.now()
        embed.set_author(
            name=self.user.name,
            icon_url=self.user.display_avatar.url
        )
        embed.set_footer(
            text=f"Requested by {user.name}\n{dt_time.hour}時{dt_time.minute}分・{dt_time.month}月{dt_time.day}日",
            icon_url=user.display_avatar.url
        )
        return embed

    def load_ch(self):
        tmp = self.um.load_user_ch(self.file)
        for n in tmp:
            if n.__str__() in self.user_list.keys():
                self.user_list[n.__str__()].set_charactor(tmp[n])
                if tmp[n] == 3:
                    self.user_list[n.__str__()].set_pitch(0.83)
            else:
                self.user_list.setdefault(n.__str__(),User(n.__str__()))
                self.user_list[n.__str__()].set_charactor(tmp[n])
                if tmp[n] == 3:
                    self.user_list[n.__str__()].set_pitch(0.83)
    
    async def setup_hook(self):
        try:
            syncd = await self.tree.sync()
            print(f"{len(syncd)}command synced")
        except Exception as e:
            print(e)

    async def on_ready(self):
        print(f'Logged on as {self.user}!')
        activity = discord.Activity(
            type=discord.ActivityType.listening,
            name="読み上げ"
        )
        await self.change_presence(activity=activity)
        #info = await self.application_info()

    async def on_message(self,message:discord.InteractionMessage):
        if message.author.bot or message.author.voice is None:
            return
        else:
            embed = self.mkembed(message.author)
            
            if message.channel.id in self.message_channel_list:
                if message.author.id.__str__() in self.user_list.keys():
                    ch = self.user_list[message.author.id.__str__()]
                else:
                    ch = self.user_list["0"]
                if message.guild.voice_client is None:
                    return
                while message.guild.voice_client.is_playing():
                    await asyncio.sleep(1)
                if message.attachments:
                    source = discord.FFmpegPCMAudio(create_wav("添付ファイル",ch))
                    embed.add_field(name="",value=f"{message.attachments}",inline=True)
                elif message.mention_everyone or message.mentions or message.role_mentions:
                    source = discord.FFmpegPCMAudio(create_wav("メンション",ch))
                    embed.add_field(name="",value=f"{message.raw_mentions}",inline=True)
                elif message.content.startswith("http"):
                    source = discord.FFmpegPCMAudio(create_wav("リンク省略",ch))
                    embed.add_field(name="",value="htt",inline=True)
                elif b"\U" in message.content.encode("unicode-escape"):
                    c_list = [c for c in message.content if not b"\U" in c.encode("unicode-escape")]
                    print(c_list)
                    if c_list.__len__() != 0:
                        text = "".join(c_list)
                        print(text)
                        source = discord.FFmpegPCMAudio(create_wav(text,ch))
                else:
                    source = discord.FFmpegPCMAudio(create_wav(message.content,ch))
                message.guild.voice_client.play(source)
            


if __name__ == "__main__":
    token = "<token>"

    intents = discord.Intents.default()
    intents.message_content = True
    intents.voice_states = True

    client = ZNDBot(intent=intents)
    client.run(token)