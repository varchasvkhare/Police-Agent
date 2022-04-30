from ast import Or
import inspect

import discord
from discord.ext import commands

class Verify(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
    
    @commands.command(name="verify")
    async def verify(self, ctx: commands.Context) -> None:
        """Server Verification"""
        class ViewWithButton(discord.ui.View):
            @discord.ui.button(style=discord.ButtonStyle.green, label='Verify')
            async def click_me_button(self, button: discord.ui.Button, interaction: discord.Interaction):
                #role = discord.utils.get(self.bot.get_guild(760134264242700320).roles, id ="903238068910309398")
                await interaction.response.send_message('Enjoy!', ephemeral=True)
                await interaction.user.add_roles(903238068910309398, reason="Pressed the verification button")
                
                
        embed = discord.Embed(
            title=f'Server Verification',
            description=inspect.cleandoc(
                f"""
                x
                
                """
            ),
            color=0x797EF6
        )
        await ctx.send(embed=embed, view=ViewWithButton())
        
async def setup(bot):
    await bot.add_cog(Verify(bot))

