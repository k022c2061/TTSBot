import discord
from discord.ext import commands
import asyncio
import re
import embed_template as em
#from create_wav_sever import CREATE_WAV
from create_wav import CREATE_WAV_roid

class MessageListenerCog(commands.Cog):
    def __init__(self,bot : commands.Bot):
        super().__init__()
        self.bot = bot

    @commands.Cog.listener("on_ready")
    async def on_ready(self):
        print("set \"MessageLisner\"")

    @commands.Cog.listener("on_message")
    async def on_message(self,ctx : discord.message.Message):
        c_id = ctx.channel.id.__str__()
        #Botの内容は無視する
        if ctx.author.bot:
            return
        #呼び出し者がVoiceChannelにいない
        elif not ctx.author.voice:
            return
        #BotがVoiceChannelにいない
        elif ctx.guild.voice_client is None:
            return
        elif c_id in self.bot.user_manager.user_data.keys():
            pass
        #読み上げ条件を満たした場合
        else:
            print(f"{ctx}\n<{ctx.channel.id}>\n{ctx.content}")
            #メッセージ内容
            context = ctx.content
            #userID
            user_id = ctx.author.id.__str__()
            #読み上げ設定の呼び出し
            if user_id in self.bot.user_data.keys():
                tts_setting = self.bot.user_data[user_id]
            else:
                tts_setting = self.bot.user_data["0"]
            #読み上げるクライアント
            voice_client = ctx.guild.voice_client
            #再生中は待機
            while voice_client.is_playing():
                asyncio.sleep(1)
            #message.contentの内容をチェック
            ##項目
            ##メッセージのテキストに変換できない文字が含まれていないかの検出
            #content = [c for c in context if not c.encode('escape-shiftjis').startswith(b'\U')]
            #context = "".join(content)
            #context = context[:10]
            ##添付ファイルの送信
            if ctx.attachments:
                #メッセージも同時に送信した場合
                if context.__len__() > 0:
                    context = context[:10] + "。添付ファイル"
                #メッセージが添付されてない場合
                else:
                    context = "添付ファイル。"
            ##Mentions
            elif ctx.mention_everyone or ctx.role_mentions or ctx.mentions or ctx.channel_mentions:
                print(context)
                context = "メンション。"
            ##Links
            elif re.match(r"*http*",context):
                context = "リンク省略。"
            ##
            else:
                pass
            #読み上げる音声のファイル生成
            source_file = CREATE_WAV_roid(context,tts_setting)
            #
            source = discord.FFmpegPCMAudio(source_file)
            #
            voice_client.play(source)
            
async def setup(bot : commands.Bot):
    await bot.add_cog(MessageListenerCog(bot))