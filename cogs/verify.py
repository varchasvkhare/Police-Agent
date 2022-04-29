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
        class Verifiction(discord.ui.View):
            def __init__(self):
                super().__init__(timeout=None)
                @discord.ui.button(label='Verify', style=discord.ButtonStyle.green, custom_id='verify')
                async def green(self, interaction: discord.Interaction, button: discord.ui.Button):
                    await interaction.response.send_message('Verification Successfull', ephemeral=True)
        
        embed = discord.Embed(
            Title = "Verification",
            description = inspect.cleandoc(
                f"""
                
                """
            )
        )
        await ctx.send(embed=embed, view=Verifiction)
        
async def setup(bot):
    await bot.add_cog(Verify(bot))

