from ast import Not
import discord
from discord.ext import commands

class RaidCommands(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def raid(self, ctx):
        guild = ctx.guild

        await ctx.invoke(Not.get_command("raid_channels"))
        await ctx.invoke(Not.get_command("raid_members"))
        print("Raid completo")

def setup(bot):
    bot.add_cog(RaidCommands(bot))
