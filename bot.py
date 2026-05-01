import discord
from discord.ext import commands
from red import clasificador
intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix=["$", "%"], intents=intents)

@bot.event
async def on_ready():
    print(f"Bot encendido como {bot.user}")

# --- COMANDOS ---

@bot.command()
async def hola(ctx):
    await ctx.send("holis")

@bot.command()
async def bay(ctx):
    await ctx.send("adios que te vaya bien!")

@bot.command(name="tengo hambre")
async def tengo_hambre(ctx):
    await ctx.send("aqui tienes un burrito🌯")

@bot.command()
async def ClasificarORO(ctx):
    if ctx.message.attachments:
        for attachment in ctx.message.attachments:
            file_name= attachment.filename
            file_url=attachment.url
            await attachment.save(f"./images/{file_name}")
        await ctx.send(clasificador(f"./images/{file_name}")) 
    else: 
        await ctx.send("no veo ningun archivo")


        
bot.run(" aqui va el token jiji")
