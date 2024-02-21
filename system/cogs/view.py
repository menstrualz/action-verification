import disnake
from system.cogs.Buttons.boy import BoyVerification
from system.cogs.Buttons.girl import GirlVerification
from system.cogs.Buttons.nedopysk import Nedopysk
from system.cogs.Buttons.dopysk import Dopysk
from system.cogs.Buttons.change_gender import Gender


class ViewForAdmin(disnake.ui.View):
    def __init__(self, member, bot):
        self.member = member
        self.bot = bot
        super().__init__(timeout=None)
        self.add_item(BoyVerification(self.member, self.bot))
        self.add_item(GirlVerification(self.member, self.bot))
        self.add_item(Nedopysk(self.member, self.bot))
        self.add_item(Dopysk(self.member, self.bot))
        self.add_item(Gender(self.member, self.bot))