import disnake
from assets.enums import Color, RolesIds


class Dopysk(disnake.ui.Button):
    def __init__(self, user, bot):
        self.user = user
        self.bot = bot
        super().__init__(label="Снять недопуск", custom_id="dopysk_button")

    async def callback(self, interaction: disnake.MessageInteraction) -> None:
        await interaction.response.defer(ephemeral=True)
        role = interaction.guild.get_role(RolesIds.NEDOPYSK)
        user = interaction.guild.get_member(self.user)
        if role in user.roles:
            await user.remove_roles(role)
            embed = disnake.Embed(color=Color.GRAY)
            embed.title = f"Снятие недопуска {user.name}"
            embed.description = f"Вы сняли недопуск у пользователя {user.mention}"
            await interaction.followup.send(embed=embed, ephemeral=True)
        else:
            embed = disnake.Embed(color=Color.GRAY)
            embed.title = f"Снятие недопуска {user.name}"
            embed.description = f"У {user.mention} нет недопуска"
            await interaction.followup.send(embed=embed, ephemeral=True)