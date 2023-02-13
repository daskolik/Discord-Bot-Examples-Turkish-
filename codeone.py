import discord
import asyncio
import datetime
import interactions
from discord import ui
import nacl
from discord.ext import commands
import socket   
keyubuvds=socket.gethostname()   
keyubuvdsipadresi=socket.gethostbyname(keyubuvds)   
adminids = "837817581507313724","1017536830545068123"
tarihsaat = datetime.datetime.now()
intentts = discord.Intents(messages=True, guilds=True, reactions=True, members=True, presences=True, message_content=True)
client = commands.Bot(command_prefix='.sk ', intents=intentts)

bottoken = 'bot token is gone here'
@client.event
async def on_ready():

    print("__________________________________BOT BİLGİLERİ___________________________________________")
    print("Bot Aktif. Botun Çalıştırıldığı saat ve tarih :", tarihsaat)
    print("token : ", bottoken)
    print("bot isim : {}".format(client.user.name))
    print("bot id : {}".format(client.user.id))
    print("server ip : "+keyubuvdsipadresi)
    print("discord version : "+ discord.__version__)
    print("                                                                  BotInfo by kolik#1337")
    print("______________________________________KONSOL______________________________________________")
    
    synced = await client.tree.sync() 
    print("[LOG:] SlashCommands Synced : " + str(len(synced)))

    ## seskanal = client.get_channel(1073336097045758054)
    ## await seskanal.connect(timeout=100000000000000000000000000000000000000000000000000000000000000000000000000000000000)
@client.event
async def on_member_join(member):
    channel = discord.utils.get(member.guild.text_channels, name="giriş-çıkış")
    await channel.send(f"{member} aramıza katıldı!")
@client.event
async def on_member_remove(member):
    channel = discord.utils.get(member.guild.text_channels, name="giriş-çıkış")
    await channel.send(f"{member} aramızdan ayrıldı :( !")

 
@client.tree.command(name="aboutbot", description="Bot hakkında genel bilgi.")
async def aboutbot(interaction: discord.Interaction):
    await interaction.response.send_message(content="skyline bot v0.0.2 # developed by kolik#1337")
@client.tree.command(name="azureee", description="cenabet azure kardeşimiz için bir komut")
async def azureee(interaction: discord.Interaction):
    await interaction.response.send_message(content="namaz kıl. cünüb gezme")


class Select(discord.ui.Select):
    def __init__(self):
        options=[
            discord.SelectOption(label="kolik#1337",emoji="👌",description="Hakkında"),
            discord.SelectOption(label="! E İ",emoji="✨",description="Hakkında"),
            discord.SelectOption(label="ASDF_ASD",emoji="🎭",description="Hakkında")
            ]       
        super().__init__(placeholder="Select an option",max_values=1,min_values=1,options=options)
    async def callback(self, interaction: discord.Interaction):
        if self.values[0] == "kolik#1337":
            await interaction.response.send_message(content="Skyline BOT un geliştiricisi ve Senior GFX Developer",ephemeral=True)
        elif self.values[0] == "! E İ":
            await interaction.response.send_message("sunucu sahibi",ephemeral=True)
        elif self.values[0] == "ASDF_ASD":
            await interaction.response.send_message("animeizleyen scripter",ephemeral=True)

class SelectView(discord.ui.View):
    def __init__(self, *, timeout = 180):
        super().__init__(timeout=timeout)   
        self.add_item(Select())
@client.command()
async def ekip(ctx):
    await ctx.send("İncelemek için tıkla!",view=SelectView(),ephemeral=True)
@client.command()
async def kolik(ctx):
    await ctx.send("amınakodumun topu")
   

client.run(bottoken)
