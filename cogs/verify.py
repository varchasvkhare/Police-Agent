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
            async def click_me_button(self, interaction: discord.Interaction, button: discord.ui.Button):
                verified=discord.utils.get(ctx.guild.roles, name="[0] Verified")
                await interaction.response.send_message('I have give you access to the server!', ephemeral=True)
                await interaction.user.add_roles(verified)
                
                
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

