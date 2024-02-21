import disnake
from disnake.ext import commands
from assets.enums import Color
from system.cogs.view import ViewForAdmin


class NaborStart(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.slash_command(name="action")
    async def nabor(self, interaction, member: disnake.Member = commands.Param(description="Участник, кого необходимо верифицировать")):
        await interaction.response.defer(ephemeral=True)
        if member.bot:
            return await interaction.followup.send("Вы не можете верифицировать бота, пробуйте человека", ephemeral=True)
   
        embed = disnake.Embed(color=Color.GRAY)
        embed.title = f"Верификация {member.name}"
        embed.add_field(name="> Зарегистрирован", value=f"```{member.created_at.strftime('%Y.%m.%d')}```")
        embed.add_field(name="** **", value="** **")
        embed.add_field(name="> Зашел на сервер", value=f"```{member.joined_at.strftime('%Y.%m.%d')}```")
        await interaction.followup.send(embed=embed, view=ViewForAdmin(member.id, self.bot))