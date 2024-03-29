import disnake
from assets.enums import Color, RolesIds


class GirlVerification(disnake.ui.Button):
    def __init__(self, user, bot):
        self.user = user
        self.bot = bot
        super().__init__(label="Девочка", custom_id="girl_button")

    async def callback(self, interaction: disnake.MessageInteraction) -> None:
        await interaction.response.defer(ephemeral=True)
        user = interaction.guild.get_member(self.user)
        role = interaction.guild.get_role(RolesIds.GIRL)
        role2 = interaction.guild.get_role(RolesIds.BOY)
        if role in user.roles or role2 in user.roles:
            embed = disnake.Embed(color=Color.GRAY)
            embed.title = f"Верификация {user.name}"
            embed.description = f"Пользователь {user.mention} уже имеет данную\nили иную роль, воспользуйтесь другими кнопками"
            await interaction.followup.send(embed=embed, ephemeral=True)
        else:
            embed = disnake.Embed(color=Color.GRAY)
            embed.title = f"Верификация {user.name}"
            embed.description = f"Вы верифицировали пользователя {user.mention} как девочку"
            await user.add_roles(role)
            await interaction.followup.send(embed=embed, ephemeral=True)