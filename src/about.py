# Built-in
import asyncio
# 3rd-party
from discord.ext import commands
# Local
import utils

class About(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(aliases=["about"])
    async def credits(self, ctx):
        """Prints information about the bot"""

        message = "\n".join([
            "The White Rabbit was created by circumspect.",
            "Source code available at https://github.com/circumspect/White-Rabbit"
        ])
        message = utils.codeblock(message)
        asyncio.create_task(ctx.send(message))
    
    @commands.command(aliases=["guide"])
    async def docs(self, ctx):
        """Link to the documentation"""

        message = "\n".join([
            "Documentation for The White Rabbit can be found here:",
            "https://white-rabbit.rtfd.io/"
        ])
        message = utils.codeblock(message)
        asyncio.create_task(ctx.send(message))


def setup(bot):
    bot.add_cog(About(bot))