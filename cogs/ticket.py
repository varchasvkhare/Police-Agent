from ast import Or
import inspect
from os import name

import discord
from discord.ext import commands

class Ticket(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
    
    @commands.command(name="ticket")
    async def ticket(self, ctx: commands.Context) -> None:
        """ticket"""
        
        class Ticket(discord.ui.View):
            @discord.ui.button(style=discord.ButtonStyle.green, label='Create a Ticket', custom_id='ticket')
            async def ticket_create_button(self, interaction: discord.Interaction, button: discord.ui.Button):
                category = discord.utils.get(ctx.guild.categories, name='⪻ᚔᚓᚒᚑ᚜office᚛ᚑᚒᚓᚔ⪼')
                mod=discord.utils.get(ctx.guild.roles, name="Moderation Team")
                
                ticket = await interaction.guild.create_text_channel(
                    category=category,
                    name=f"Ticket-{interaction.user.id}",
                    overwrites={
                        interaction.guild.default_role: discord.PermissionOverwrite(view_channel=False),
                        interaction.user: discord.PermissionOverwrite(view_channel=True),
                        mod: discord.PermissionOverwrite(view_channel=True)
                    }
                )
                
                await interaction.response.send_message(f'ticket created in <#{ticket.id}>', ephemeral=True)
        
        embed = discord.Embed(
            title=f'Create a Ticket',
            description=inspect.cleandoc(
                f"""
                • Write your issue as soon as you open a ticket instead of waiting for a mod to ping you.
                • Don't open a ticket for no reason
                • Don't open a ticket without typing your query and not respond.
                • Don't DM or Ping mods when they do not respond instantaneously.
                
                To Create a Ticket press the button below
                """
            ),
            color=0x111111
        )
        embed.set_footer(
            text='Opening tickets for trolling or for no purpose might get you punished, punishments include mute, warn and ban.'
        )
        await ctx.send(embed=embed, view=Ticket())
        
async def setup(bot):
    await bot.add_cog(Ticket(bot))

