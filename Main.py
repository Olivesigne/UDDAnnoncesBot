import os
import discord
from discord.ext import commands

token = os.environ['TOKEN']
intents = discord.Intents.all()
intents.message_content = True
intents.members = True
intents.guilds = True
bot = commands.Bot(command_prefix="/", intents=intents)

#Variables
annonces = 1296193808236806238
uddId = 1271185905520082969
leId = 1128719599811178577

@bot.event
async def on_ready():
    print(f"Connecté en tant que {bot.user}")
    synced = await bot.tree.sync()
    print(f"{len(synced)} commande(s) synchronisée(s)")

@bot.tree.command(name="annonce", description="Poste une annonce")
async def annonce(interaction: discord.Interaction, channel: discord.TextChannel, mention: discord.Role, message: str):
    await interaction.response.defer()
    idUser = interaction.user.id
    if idUser == uddId or idUser == leId:
        chars = '(\'\',)'
        translatedMessage = str(message).translate(str.maketrans('', '', chars))
        await channel.send(f"{mention.mention}, \n{translatedMessage}")
    else:
        await interaction.followup.send("Désolé, vous n'avez pas la permission d'exécuter cette commande :man_shrugging:")

@bot.event
async def on_message(message):
    channelId = int(message.channel.id)
    if channelId == annonces:
        derniereAnnonce = str(message.content)
        if os.path.exists("annonces.txt"):
            fichierAppend = open("annonces.txt", "a")
            fichierRead = open("annonces.txt", "r")
            fichierAppend.write('\n' + derniereAnnonce)
        else:
            fichierCreate = open("annonces.txt", "x")
            fichierRead = open("annonces.txt", "r")
            fichierCreate.write(derniereAnnonce)

bot.run(token)