from logging import info, warning, error, critical
from discord import Intents, Message
from discord.ext import commands
from bot import CONFIG
from bot.help import Help
from bot.helpers.color_helper import get_color_digit


class Grace(commands.Bot):
    def __init__(self):
        super().__init__(
            command_prefix=CONFIG.bot.prefix,
            description="Grace is the official Code Society Discord bot.",
            help_command=Help(),
            intents=Intents.all()
        )

    @property
    def default_color(self):
        return get_color_digit(CONFIG.style.embed_color)

    def load_extensions(self, extensions):
        for extension in extensions:
            info(f"Loading {extension}")
            self.load_extension(extension)

    async def on_ready(self):
        info(f"{self.user.name}#{self.user.id} is online and ready to use!")
