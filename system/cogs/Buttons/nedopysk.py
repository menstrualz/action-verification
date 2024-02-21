import disnake
from assets.enums import Color, RolesIds


class Nedopysk(disnake.ui.Button):
    def __init__(self, user, bot):
        self.user = user
        self.bot = bot
        super().__init__(label="Выдать недопуск", custom_id="nedopysk_button")

    async def callback(self, interaction: disnake.MessageInteraction) -> None:
        await interaction.response.defer(ephemeral=True)
        role = interaction.guild.get_role(RolesIds.NEDOPYSK)
        user = interaction.guild.get_member(self.user)
        if role in user.roles:
            embed = disnake.Embed(color=Color.GRAY)
            embed.title = f"Выдача недопуска {user.name}"
            embed.description = f"У {user.mention} уже есть недопуск"
            await interaction.followup.send(embed=embed, ephemeral=True)
        else:
            await user.add_roles(role)
            embed = disnake.Embed(color=Color.GRAY)
            embed.title = f"Выдача недопуска {user.name}"
            embed.description = f"Вы выдали недопуск {user.mention}"
            await interaction.followup.send(embed=embed, ephemeral=True)