import discord
from discord import Forbidden, message
from discord.ext import commands
from discord.ext import commands
from discord.ext.commands import has_permissions, MissingPermissions
from discord.utils import get

#slash commands
from discord import app_commands, Intents, Client, Interaction
import inspect

#class to implement 
class SlashCMD(Client):
    def __init__(self, *, intents: Intents):
        super().__init__(intents=intents)
        self.tree = app_commands.CommandTree(self)

    async def setup_hook(self) -> None:
        """ This is called when the bot boots, to setup the global commands """
        await self.tree.sync(guild=None)

bot = SlashCMD(intents=Intents.none())

@bot.event
async def on_ready():
    print(f' ✅ {bot.user.name} is online and connected')
    print(f" ✅ {bot.user.name} is now awake to help her master")
    print("--------------------------------------------------------------------------------------------------------------------------")

#actual slash command
@bot.tree.command()
async def hello(interaction: Interaction):
    """ Says hello or something idk""" #the litttle description under the name
    # Then responds in the channel with this message
    await interaction.response.send_message(inspect.cleandoc(f"Heyo **{interaction.user}**, Have a very nice day ^^"))
    
#user input 
@bot.tree.command()
async def userinput(interaction: Interaction, *, your_text: str):
    """user input command"""
    await interaction.response.send_message(f"**You said: ** {your_text}")

bot.run('TOKEN')
