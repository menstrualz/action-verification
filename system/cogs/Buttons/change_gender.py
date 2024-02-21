import disnake
from assets.enums import Color, RolesIds


class Gender(disnake.ui.Button):
    def __init__(self, user, bot):
        self.user = user
        self.bot = bot
        super().__init__(label="Сменить гендер", custom_id="gender_button")

    async def callback(self, interaction: disnake.MessageInteraction) -> None:
        await interaction.response.defer(ephemeral=True)
        user = interaction.guild.get_member(self.user)
        role_girl = interaction.guild.get_role(RolesIds.GIRL)
        role_boy = interaction.guild.get_role(RolesIds.BOY)
        if role_girl in user.roles:
            await user.remove_roles(role_girl)
            await user.add_roles(role_boy)
            embed = disnake.Embed(color=Color.GRAY)
            embed.title = f"Смена гендера {user.name}"
            embed.description = f"Пользователь {user.mention} теперь пол мальчика"
            await interaction.followup.send(embed=embed, ephemeral=True)
        elif role_boy in user.roles:
            await user.remove_roles(role_boy)
            await user.add_roles(role_girl)
            embed = disnake.Embed(color=Color.GRAY)
            embed.title = f"Смена гендера {user.name}"
            embed.description = f"Пользователь {user.mention} теперь пол девочки"
            await interaction.followup.send(embed=embed, ephemeral=True)
        else:
            embed = disnake.Embed(color=Color.GRAY)
            embed.title = f"Смена гендера {user.name}"
            embed.description = f"Пользователь {user.mention} не имеет никакой роли"
            await interaction.followup.send(embed=embed, ephemeral=True)