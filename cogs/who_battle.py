import disnake
from disnake.ext import commands

import settings

class cog_template(commands.Cog):
    def __init__(self, bot:commands.Bot):
        self.bot = bot
        self.log = settings.logging.getLogger('bot')
        self.battle_data = []

    @commands.slash_command(description="say you are ready to battle")
    async def available_to_battle(self, inter:disnake.AppCmdInter) -> None:
        self.battle_data.append(inter.user.id)
        await inter.response.send_message("You are available to battle")

    @commands.slash_command(description="say you are no longer available to battle")
    async def cant_battle_anymore(self, inter:disnake.AppCmdInter) -> None:
        self.battle_data.remove(inter.user.id)
        await inter.response.send_message("You are no longer available to battle")

    @commands.slash_command(description="show who's available to battle")
    async def see_who_can_battle(self, inter:disnake.AppCmdInter) -> None:

        battlers:str = ""
        for user in self.battle_data:
            member = inter.guild.get_member(user).display_name
            battlers += f"{inter.guild.get_member(user).display_name}\n"

        embed = disnake.Embed(
            colour=disnake.Colour.dark_blue(),
            title="Who Can Battle"
        )

        embed.set_thumbnail(url="https://media.discordapp.net/attachments/1112206680613191741/1131436082270056549/Full_Art_Lucario.png?width=1310&height=982")
        embed.set_image(url="https://media.tenor.com/prG1R7PoHJQAAAAC/mega-rayquaza.gif")

        embed.add_field(name="Battle Me", value=battlers)
        await inter.response.send_message(embed=embed)


def setup(bot: commands.Bot):
    bot.add_cog(cog_template(bot))
