import logging
from discord.ext import commands


logger = logging.getLogger(__name__)


async def is_admin(ctx) -> bool:
    """
    Only an admin can sync guild commands.
    Doing this too much will cause a ratelimit
    """
    return ctx.message.author.guild_permissions.administrator


class CommandSync(commands.Cog):
    def __init__(self, bot: commands.Bot) -> None:
        self.bot = bot

    @commands.command(name="sync")
    @commands.check(is_admin)
    async def sync(self, ctx):
        synced = await self.bot.tree.sync(guild=ctx.guild)
        logger.info(f"Synced {len(synced)} command(s) with Discord.")
        logger.info(f"Commands: {synced}")

    @sync.error
    async def sync_error(self, ctx, error):
        if isinstance(error, commands.CheckFailure):
            # This only happens when a user who does not have Admin tries to use this command.
            await ctx.send('Oie, you cant use that.')


async def setup(bot: commands.Bot) -> None:
    await bot.add_cog(CommandSync(bot))
