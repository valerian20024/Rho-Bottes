import discord
from discord.ext import commands

class UtilsCog(commands.Cog):
    def __init__(self, bot: commands.Bot):
        self.bot = bot
    
    @commands.command()
    async def halp(self, ctx: commands.Context):
        return await ctx.send("Commands available are !rand, !randColor, and !hello")        
    
    @commands.command()
    async def nyoto(self, ctx: commands.Context):
        greeting = "🇲🇽🌽🌮 OH OUI MON BEAU MEXICAAIN JAJAJAJAJAJ 🌽🌮🇲🇽"
        return await ctx.send(greeting)

async def setup(bot: commands.Bot):
    await bot.add_cog(UtilsCog(bot))  