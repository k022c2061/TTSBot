from discord import User,Member,Embed
from datetime import datetime

color = [    
    0x90ee90,
    0xdc143c,
]
'''
embed color

List
-----
0:success
1:error
'''


def embed_template(bot :User | Member,user : User | Member) -> Embed:
    '''
    create template of embed

    Return
    ------
    discord.Embed object
    '''
    embed = Embed(
        color=color[1]
    )
    dt = datetime.now()
    embed.set_author(
        name=bot.name,
        icon_url=bot.display_avatar.url
    )
    embed.set_footer(
        text=f"Requested by {user.display_name}\n{dt.hour}時{dt.minute}分・{dt.month}月{dt.day}日",
        icon_url=user.display_avatar.url
    )
    return embed