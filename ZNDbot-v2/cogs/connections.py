from discord.ext import commands
from discord import app_commands,Interaction,Embed,FFmpegPCMAudio,Member
import embed_template as em
from create_wav import CREATE_WAV_roid

class ConnectionCog(commands.Cog):
    def __init__(self,bot : commands.Bot):
        super().__init__()
        self.bot = bot
        #データを登録
        self.users_data : dict = self.bot.user_manager.user_data

    @commands.Cog.listener("on_ready")
    async def on_ready(self):
        print("set \"zJoin & zDisconnect\" command")

    @app_commands.command(name="zjoin",description="現在のボイスチャンネルに接続します")
    async def srash_zjoin(self,ctx:Interaction):
        #defer
        await ctx.response.defer()
        #InteractしたUserID
        ctx_user_id = ctx.user.id.__str__()
        #Embedの発行
        embed = em.embed_template(self.bot.user,ctx.user)
        #読み上げるテキスト
        context = "接続しました"
        #接続に関する動作
        ##項目
        ##ボイスチャンネルに既に接続されているか
        ##ボスチャンネルに呼び出したユーザーが接続しているか
        try:
            #ユーザーがボイスに接続されていない
            if ctx.user.voice is None:
                embed.add_field(name="",value=f"**{ctx.user.mention}はボイスチャンネルに接続されていません**",inline=True)
            #既に接続されている
            elif ctx.guild.voice_client:
                embed.add_field(name="",value=f"**{self.bot.user.mention}は既にボイスチャンネルに接続されています**")
                embed.add_field(name="接続されているチャンネル",value=f"**{ctx.guild.voice_client.channel.jump_url}**")
            #
            else:
                #userデータのチェック
                if ctx_user_id in self.users_data.keys():
                    source_file = CREATE_WAV_roid(context,self.users_data[ctx_user_id])
                else:
                    source_file = CREATE_WAV_roid(context,self.users_data["0"])
                embed.add_field(name="接続しました",value=f"{ctx.user.voice.channel.jump_url}に接続しました",inline=True)
                #VC接続
                voice_client = await ctx.user.voice.channel.connect()
                source = FFmpegPCMAudio(source_file)
                #音声再生
                voice_client.play(source)
        except Exception as e:
            embed.clear_fields()
            embed.add_field(name="処理に失敗しました",value="")
            print(f"srash_zjoin command Exception:{e}")
            await ctx.followup.send(embed=embed,ephemeral=True)
        else:
            embed.color = em.color[0]
            await ctx.followup.send(embed=embed)
        finally:
            pass

    @app_commands.command(name="zdisconnect",description="現在のボイスチャンネルから切断します")
    async def srash_disconnect(self,ctx : Interaction):
        try:
            await ctx.response.defer()
            embed = em.embed_template(self.bot.user,ctx.user)
            await ctx.guild.voice_client.disconnect()
        except Exception as e:
            print(f"srash_disconnect command Exception:{e}")
        finally:
            await ctx.followup.send(embed=embed)

    #description="チャット専用チャンネルを作成しボイスチャンネルに呼び出します"
    #理想:ボットのメニューから呼び出しコマンドの実行
    #コンテクストメニューの表示をボットのみにしたい
    #ほぼ現状不可能→代替としてBotのDescriptionにコマンドとコマンドIDを埋め込むことで対応可能

async def setup(bot : commands.Bot):
    await bot.add_cog(ConnectionCog(bot))