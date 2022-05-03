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
            @discord.ui.button(
                style = discord.ButtonStyle.green,
                label = 'Giveaways Access',
                custom_id = 'gaw_access',
                emoji = '<:gaw:971001484261064726>'
            )
            async def gaw_access_button(
                self,
                interaction: discord.Interaction,
                button: discord.ui.button
            ):
                gaw_access = discord.utils.get(ctx.guild.roles, name="Giveaway Access")
                gaw_bl = discord.utils.get(ctx.guild.roles, name = 'Giveaway Blacklist')
                
                if gaw_bl in interaction.user.roles:
                    await interaction.response.send_message('Hold on bro! You are blacklisted from giveaways so i cant hand over this role to you.', ephemeral=True)
                elif gaw_access in interaction.user.roles:
                    await interaction.response.send_message(f'I have removed {gaw_access.mention} from you', ephemeral=True)
                    await interaction.user.remove_roles(gaw_access)
                else:
                    await interaction.response.send_message(f'I have added {gaw_access.mention} to you', ephemeral=True)
                    await interaction.user.add_roles(gaw_access)
                      
            @discord.ui.button(
                style=discord.ButtonStyle.green,
                label='Event Access',
                custom_id='event_access',
                emoji='<:event:971001579593428992>'
            )
            async def event_access_button(
                self,
                interaction: discord.Interaction,
                button: discord.ui.Button
            ):
                event_access = discord.utils.get(ctx.guild.roles, name="Event Access")
                event_bl = discord.utils.get(ctx.guild.roles, name = 'Event Blacklist')
                
                if event_bl in interaction.user.roles:
                    await interaction.response.send_message('Hold on bro! You are blacklisted from events so i cant hand over this role to you.', ephemeral=True)
                elif event_access in interaction.user.roles:
                    await interaction.response.send_message(f'I have removed {event_access.mention} from you', ephemeral=True)
                    await interaction.user.remove_roles(event_access)
                else:
                    await interaction.response.send_message(f'I have added {event_access.mention} to you', ephemeral=True)
                    await interaction.user.add_roles(event_access)
            
            @discord.ui.button(
                style=discord.ButtonStyle.green,
                label='Bot Channel Access',
                custom_id='bot_access',
                emoji='<:bota:971001648786837564>'
            )
            async def bot_access_button(
                self,
                interaction: discord.Interaction,
                button: discord.ui.Button
            ):
                bot_access = discord.utils.get(ctx.guild.roles, name="Event Access")
                
                if bot_access in interaction.user.roles:
                    await interaction.response.send_message(f'I have removed {bot_access.mention} from you', ephemeral=True)
                    await interaction.user.remove_roles(bot_access)
                else:
                    await interaction.response.send_message(f'I have added {bot_access.mention} to you', ephemeral=True)
                    await interaction.user.add_roles(bot_access)
        

                
                
        embed = discord.Embed(
            #title=f'Ping roles below dummy',
            description=inspect.cleandoc(
                f"""
                **Access Roles -**
                
                ・Giveaway Access - Access to giveaway channels
                ・Event Access - Access to event channels
                ・Bot Access - Access to all bot channels
                
                **Ping Roles -**
                
                ・Announcements - Get notified on any server updates, staff applications etc
                ・Status - Get notified on bot's uptime and downtime
                ・Partnership - Get pinged whenever we partner with a server
                ・Giveaways - Get pinged on any ongoing giveaway
                ・Events - Get notified on any ongoing event
                """
            ),
            color=0xfcf55f
        )
        await ctx.send(embed=embed, view=Announcements())
        
async def setup(bot):
    await bot.add_cog(SelfRoles(bot))

