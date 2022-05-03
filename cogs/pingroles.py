from ast import Or
import inspect

import discord
from discord.ext import commands

class PingRoles(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
    
    @commands.command(name="pingroles")
    @commands.check_any(
        commands.has_any_role(903238046323998720),
        commands.has_permissions(administrator=True)
    )
    async def pingroles(self, ctx: commands.Context) -> None:
        """ping roles"""
        class Announcements(discord.ui.View):
            @discord.ui.button(style=discord.ButtonStyle.blurple, label='Announcements', custom_id='announcements', emoji='<:announcements:970937379839967332>')
            async def verification_button(self, interaction: discord.Interaction, button: discord.ui.Button):
                announcement=discord.utils.get(ctx.guild.roles, name="• ❯ Announcements")
                if announcement in interaction.user.roles:
                    await interaction.response.send_message(f'I have removed {announcement.mention} from you', ephemeral=True)
                    await interaction.user.remove_roles(announcement)
                else:
                    await interaction.response.send_message(f'I have added {announcement.mention} to you', ephemeral=True)
                    await interaction.user.add_roles(announcement)
        
        #class Giveaways(discord.ui.view):
            @discord.ui.button(style=discord.ButtonStyle.blurple, label='Giveaways', custom_id='giveaways', emoji='<:announcements:970937379839967332>')
            async def verification_button(self, interaction: discord.Interaction, button: discord.ui.Button):
                gaws=discord.utils.get(ctx.guild.roles, name="• ❯ Giveaways")
                if gaws in interaction.user.roles:
                    await interaction.response.send_message(f'I have removed {gaws.mention} from you', ephemeral=True)
                    await interaction.user.remove_roles(gaws)
                else:
                    await interaction.response.send_message(f'I have added {gaws.mention} to you', ephemeral=True)
                    await interaction.user.add_roles(gaws)
                
                
        embed = discord.Embed(
            title=f'Ping roles below dummy',
            description=inspect.cleandoc(
                f"""
                
                """
            ),
            color=0x111111
        )
        await ctx.send(embed=embed, view=Announcements())
        
async def setup(bot):
    await bot.add_cog(PingRoles(bot))

