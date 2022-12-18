import discord
from discord import Forbidden, message
from discord.ext import commands
from discord.ext import commands
from discord.ext.commands import has_permissions, MissingPermissions
from discord.utils import get
import pyfiglet

#slash commands
import aiohttp
import random
from discord import app_commands, Intents, Client, Interaction
import inspect
import time

#class to implement 
class FunnyBadge(Client):
    def __init__(self, *, intents: Intents):
        super().__init__(intents=intents)
        self.tree = app_commands.CommandTree(self)

    async def setup_hook(self) -> None:
        """ This is called when the bot boots, to setup the global commands """
        await self.tree.sync(guild=None)

bot = FunnyBadge(intents=Intents.none())

@bot.event
async def on_ready():
    print(pyfiglet.figlet_format(f"{bot.user.name}"))
    print(f' ✅ {bot.user.name} is online and connected')
    print(f" ✅ {bot.user.name} is now awake to help her master")
    print("--------------------------------------------------------------------------------------------------------------------------")

#actual slash command
@bot.tree.command()
async def hello(interaction: Interaction):
    """ Says hello or something idk""" #the litttle description under the name
    # Then responds in the channel with this message
    await interaction.response.send_message(inspect.cleandoc(f"Heyo **{interaction.user}**, Have a very nice day ^^"))

#swimsuit
@bot.tree.command()
async def swimsuit(interaction: Interaction):
    """sexy swimsuit pic"""
    embed = discord.Embed(title="", description="")

    async with aiohttp.ClientSession() as cs:
        async with cs.get('https://www.reddit.com/r/swimsuithentai/new.json?sort=hot%27') as r:
            res = await r.json()
            embed.set_image(url=res['data']['children'] [random.randint(0, 25)]['data']['url'])
            await interaction.response.send_message(embed=embed)

#gayrate
@bot.tree.command()
async def gaytest(interaction: Interaction, user: discord.Member):
    """test your gayrat"""
    random_number = random.randint(10, 100)
    result0 = random_number <= 50
    result1 = random_number > 50

    if result0:
        embed0 = discord.Embed(title=f'{"🏳️‍🌈"} __{user.name}__ you are to `{random_number}%` gay \n hmm doesnt seem very gay', color=0x2ecc71)
        await interaction.response.send_message(embed=embed0)
    if result1:
        embed1 = discord.Embed(title=f'{"🏳️‍🌈"} __{user.name}__ you are to `{random_number}%` gay \n oh sh!t you look very gay wanna have some yaoi?', color=0x2ecc71)
        await interaction.response.send_message(embed=embed1)

#dicksize
@bot.tree.command()
async def dicksize(interaction: Interaction, user: discord.Member):
    """how long is your's?"""
    text = "8{}D".format("=" * random.randint(0, 20))
    embed = discord.Embed(title=f"*{user.name}'s* dick is:", description=text)
    await interaction.response.send_message(embed=embed)

@bot.tree.command()
@commands.has_permissions(administrator=True)
async def vmute(ctx, user: discord.Member=None):
    await user.edit(mute = True)
    await interaction.response.send_message(f":mute: {user.mention} you got muted by {ctx.author.mention}")

#openai api
key = "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"
import openai

#aichat
@bot.tree.command()
async def aichat(interaction: Interaction, *, term: str):
    """text with the bot's AI"""
    openai.api_key = key
    response = openai.Completion.create(
        model="text-davinci-003",
        prompt=f"{term}",
        temperature=0.5,
        max_tokens=60,
        top_p=0.3,
        frequency_penalty=0.5,
        presence_penalty=0.0
    )
    response_lmao = response['choices'][0]['text']
    await interaction.response.send_message(f"```{response_lmao}```")

#aipic
@bot.tree.command()
async def aipic(interaction: Interaction, *, term: str):
    """Let the bot's AI generate images"""

    openai.api_key = key
    response = openai.Image.create(
                prompt=f"{term}",
                n=1,
                size="1024x1024"
            )
    image_url = response['data'][0]['url']
    print(image_url)
    await interaction.response.send_message(embed=embed)


bot.run('OTU4NDczNDMwMjc2MTMyOTc2.G42MVl.VUihGFLyN1E-yILcmppHeE5pZWyP_D3_iTaKa8')
#https://discord.com/invite/A8jAmk6bjt