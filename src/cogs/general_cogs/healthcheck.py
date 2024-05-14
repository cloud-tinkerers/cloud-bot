import logging
import discord
from discord.ext import commands



# We add our logger to the cog.
logger = logging.getLogger(__name__)


class Healthcheck(discord.ext.commands.Cog):
    """
    All cogs are added into their own class.
    If an error occurs in the cog, the cog itself will fail and restart.
    It will NOT bring down the bot with it.
    """
    def __init__(self, bot: commands.Bot) -> None:
        """ Initialize the class using the bot object from __main__ """
        self.bot = bot

    @discord.app_commands.command(name="ping")
    async def ping(self, interaction: discord.Interaction):
        logger.info(f"ping command used by {interaction.user.name}")

        shit_speed = f"{str(round(self.bot.latency * 1000))} ms"
        embed = discord.Embed(title="**Pong!**", description="**" + shit_speed + "**", color=0xafdafc)
        await interaction.response.send_message(embed=embed)


async def setup(bot: commands.Bot) -> None:
    """ Cogs setup functions are mandatory for cog initialization"""
    await bot.add_cog(Healthcheck(bot))
