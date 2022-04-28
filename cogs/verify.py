from ast import Or
import inspect

import discord
from discord.ext import commands

class Rules(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
    
    @commands.command(name="verify")
    async def rules(self, ctx: commands.Context) -> None:
        """Some Server Rules"""
        class ViewWithButton(discord.ui.View):
            @discord.ui.button(style=discord.ButtonStyle.blurple, label='Verify')
            async def click_me_button(self, button: discord.ui.Button, interaction: discord.Interaction):
                await ctx.add_roles(ctx, 903238068910309398)
        
        embed = discord.Embed(
            title=f'Server Verification',
            description=inspect.cleandoc(
                f"""
                
                
                """
            ),
            color=0x797EF6
        )
        await ctx.send(embed=embed, view=ViewWithButton())
        
async def setup(bot):
    await bot.add_cog(Rules(bot))

