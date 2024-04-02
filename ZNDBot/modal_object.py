from discord import ui,Interaction,TextStyle,Embed,User,Member
import random

class MakeRandomTeam(ui.Modal):
    def __init__(self,title,_list,embed:Embed):
        super().__init__(
            title=title
        )

        self.team_count = ui.TextInput(
            label="チームの数",
            required=True,
            max_length=1,
            default=2,
            style=TextStyle.short
        )

        self.team_member = ui.TextInput(
            label="チームメンバーの人数",
            max_length=1,
            required=True,
            style=TextStyle.short,
            placeholder="チームメンバーの数を入力してください"
        )

        self.add_item(self.team_count)
        self.add_item(self.team_member)

        self.member_list = _list
        self.embed = embed

    async def on_submit(self,ctx:Interaction):
        try:
            team_member = list()
            team_cnt = int(self.team_count.value)
            member_cnt = int(self.team_member.value)
            cnt = len(self.member_list)
            if cnt < team_cnt*team_member:
                self.embed.add_field(name="入力した数値に問題があります",value="",inline=True)
                raise Exception("指定した数値に問題があります")
            for n in range(team_cnt):
                for m in range(member_cnt):
                    rslt = random.choice(self.member_list)
                    self.member_list.pop(self.member_list.index(rslt))
                    team_member.append(rslt)
                    team_member_str = "\n".join(team_member)
                self.embed.add_field(name=f"チーム{n + 1}",value=f"{team_member_str}",inline=False)
                team_member.clear()
            last_member = "\n".join(self.member_list)
            self.embed.add_field(name="観戦",value=last_member,inline=True)
        except Exception as e:
            print(e)
            self.embed.color = 0xdc143c #CurimzonColor
            self.embed.add_field(name="不正確な入力のためチーム作成を行えませんでした",value="",inline=True)
        finally:
            await ctx.response.send_message(embed=self.embed)