from discord.ext import commands
from discord import app_commands
from discord import Interaction
import embed_template as em

class ReloadCog(commands.Cog):
    def __init__(self,bot : commands.Bot):
        super().__init__()
        self.bot = bot

    @commands.Cog.listener("on_ready")
    async def on_ready(self):
        print("set \"reload\" command")

    @app_commands.command(name="reload",description="Debug用")
    async def Reload(self,ctx : Interaction):
        embed = em.embed_template(self.bot.user,ctx.user)
        user_id = ctx.user.id.__str__()
        try:
            if user_id not in ["774539378961022996","317550146604761089"]:
                raise Exception("not has permissions")
            embed.color = em.color[0]
        except Exception as e :
            embed.add_field(name="Exception",value=f"{type(e)}\n{e}")
        finally :
            await ctx.response.send_message(embed=embed,ephemeral=True)

async def setup(bot : commands.Bot):
    await bot.add_cog(ReloadCog(bot))