import discord
from discord.ext import commands
import os

class GreetingCog(commands.Cog):
    def __init__(self, bot: commands.Bot) -> None:
        self.bot = bot

    @commands.command()
    async def hello(self, ctx: commands.Context) -> discord.Message:
        return await ctx.send("Hello 👋")
    
    @commands.hybrid_command()
    async def test(seld, ctx):
        return await ctx.send("A hybrid command?")

async def setup(bot: commands.Bot) -> None:
    await bot.add_cog(GreetingCog(bot), guild=discord.Object(id=os.getenv("GUILD_ID")))