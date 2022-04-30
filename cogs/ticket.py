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
                
                await interaction.guild.create_text_channel(
                    category=category,
                    name=f"Ticket-{interaction.user.id}",
                    overwrites={
                        interaction.guild.default_role: discord.PermissionOverwrite(view_channel=False),
                        interaction.user: discord.PermissionOverwrite(view_channel=True),
                        mod: discord.PermissionOverwrite(view_channel=True)
                    }
                )
                ticket_name=discord.utils.get(ctx.guild.channels, f"Ticket-{interaction.user.id}")
                await interaction.response.send_message(f'e {ticket_name}', ephemeral=True)
        
        embed = discord.Embed(
            title=f'Create a Ticket',
            description=inspect.cleandoc(
                f"""
                
                """
            ),
            color=0x111111
        )
        await ctx.send(embed=embed, view=Ticket())
        
async def setup(bot):
    await bot.add_cog(Ticket(bot))

