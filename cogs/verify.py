from ast import Or
import inspect

import discord
from discord.ext import commands

class Verify(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
    
    @commands.command(name="verify")
    @commands.check_any(
        commands.has_any_role(903238046323998720),
        commands.has_permissions(administrator=True)
    )
    async def verify(self, ctx: commands.Context) -> None:
        """Server Verification"""
        class Verify(discord.ui.View):
            @discord.ui.button(style=discord.ButtonStyle.green, label='Verify', custom_id='verify')
            async def verification_button(self, interaction: discord.Interaction, button: discord.ui.Button):
                verified=discord.utils.get(ctx.guild.roles, name="[0] Verified")
                await interaction.response.send_message('I have given you access to the server!', ephemeral=True)
                await interaction.user.add_roles(verified)
                
                
        embed = discord.Embed(
            title=f'Server Verification',
            description=inspect.cleandoc(
                f"""
                If you have successfully read the above rules then click the button below to get verified.
                In case if the button is not working open a ticken in <#969952359407030322>
                
                """
            ),
            color=0x111111
        )
        await ctx.send(embed=embed, view=Verify())
        
async def setup(bot):
    await bot.add_cog(Verify(bot))

