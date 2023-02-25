from discord.ext import commands

class WhiteRabbit(commands.Bot):
    async def setup_hook(self) -> None:
        PLUGINS = ["about", "admin", "debug", "export", "game", "manual", "players", "settings"]
        for plugin in PLUGINS:
            await self.load_extension(f"cogs.{plugin}")