from ast import Or
import inspect

import discord
from discord.ext import commands

class SelfRoles(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
    
    @commands.command(name="selfroles")
    @commands.check_any(
        commands.has_any_role(903238046323998720),
        commands.has_permissions(administrator=True)
    )
    async def selfroles(self, ctx: commands.Context) -> None:
        """ping roles"""
        class Announcements(discord.ui.View):
            @discord.ui.button(style=discord.ButtonStyle.blurple, label='Announcements', custom_id='announcements', emoji='<:announcements:970937379839967332>')
            async def announcement_button(self, interaction: discord.Interaction, button: discord.ui.Button):
                announcement=discord.utils.get(ctx.guild.roles, name="• ❯ Announcements")
                if announcement in interaction.user.roles:
                    await interaction.response.send_message(f'I have removed {announcement.mention} from you', ephemeral=True)
                    await interaction.user.remove_roles(announcement)
                else:
                    await interaction.response.send_message(f'I have added {announcement.mention} to you', ephemeral=True)
                    await interaction.user.add_roles(announcement)
        
            @discord.ui.button(style=discord.ButtonStyle.blurple, label='Giveaways', custom_id='giveaways', emoji='<a:giveaways:970959495708676146>')
            async def gaw_button(self, interaction: discord.Interaction, button: discord.ui.Button):
                gaws=discord.utils.get(ctx.guild.roles, name="• ❯ Giveaways")
                if gaws in interaction.user.roles:
                    await interaction.response.send_message(f'I have removed {gaws.mention} from you', ephemeral=True)
                    await interaction.user.remove_roles(gaws)
                else:
                    await interaction.response.send_message(f'I have added {gaws.mention} to you', ephemeral=True)
                    await interaction.user.add_roles(gaws)
                    
            @discord.ui.button(style=discord.ButtonStyle.blurple, label='Events', custom_id='events', emoji='<a:giveaways:970959495708676146>')
            async def gaw_button(self, interaction: discord.Interaction, button: discord.ui.Button):
                event=discord.utils.get(ctx.guild.roles, name="• ❯ Events")
                if event in interaction.user.roles:
                    await interaction.response.send_message(f'I have removed {event.mention} from you', ephemeral=True)
                    await interaction.user.remove_roles(event)
                else:
                    await interaction.response.send_message(f'I have added {event.mention} to you', ephemeral=True)
                    await interaction.user.add_roles(event)
                    
            @discord.ui.button(style=discord.ButtonStyle.blurple, label='Status', custom_id='status', emoji='<a:giveaways:970959495708676146>')
            async def gaw_button(self, interaction: discord.Interaction, button: discord.ui.Button):
                sta=discord.utils.get(ctx.guild.roles, name="• ❯ Status")
                if sta in interaction.user.roles:
                    await interaction.response.send_message(f'I have removed {sta.mention} from you', ephemeral=True)
                    await interaction.user.remove_roles(sta)
                else:
                    await interaction.response.send_message(f'I have added {sta.mention} to you', ephemeral=True)
                    await interaction.user.add_roles(sta)
                
                
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
    await bot.add_cog(SelfRoles(bot))

