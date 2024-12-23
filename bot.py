import os
import discord
from discord.ext import commands

# Carregar o token do bot a partir das variáveis de ambiente
TOKEN = os.getenv("DISCORD_TOKEN")

# Configurar as intenções necessárias
intents = discord.Intents.default()

# Criar o bot
bot = commands.Bot(command_prefix="!", intents=intents)

# Evento de prontidão (quando o bot estiver online)
@bot.event
async def on_ready():
    print(f"Bot conectado como {bot.user}")

# Comando ping
@bot.command()
async def ping(ctx):
    latency = round(bot.latency * 1000)  # Latência em ms
    await ctx.send(f"Pong! 🏓 Latência: {latency}ms")

# Rodar o bot
bot.run(TOKEN)
