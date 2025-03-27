import discord
from discord.ext import commands
import os

TOKEN = "%TOKEN%" 
GUILD_ID = "%SERVIDOR%"   

intents = discord.Intents.default()
intents.guilds = True
intents.messages = True
intents.members = True
bot = commands.Bot(command_prefix="%", self_bot=True, intents=intents)

for filename in os.listdir("./cogs"):
    if filename.endswith(".py"):
        bot.load_extension(f"cogs.{filename[:-3]}")

@bot.event
async def on_ready():
    print(f"Nome do bot: {bot.user.name}")
    print(f"ID do Bot: {bot.user.id}")
    print("------")

    guild = bot.get_guild(int(GUILD_ID))
    if not guild:
        print("Erro no ID")
        return

    print(f"Servidor encontrado: {guild.name} (ID: {guild.id})")
    if guild.get_member(bot.user.id) is None:
        print("O bot no está no servidor")
        return

    await bot.close()

if __name__ == "__main__":
    print("Infernum Squad Self$ Bot by Self was here")
bot.run("TOKEN", bot=False, reconnect=True)

