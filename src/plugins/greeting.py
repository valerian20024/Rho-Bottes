import discord
from discord.ext import commands
import os
import asyncio

class GreetingCog(commands.Cog):
    def __init__(self, bot: commands.Bot) -> None:
        self.bot = bot

    @commands.command()
    async def hello(self, ctx: commands.Context) -> discord.Message:
        return await ctx.send("Hello 👋")
    
    @commands.hybrid_command()
    async def test(self, ctx):
        async with ctx.channel.typing():
            await asyncio.sleep(25)
        await ctx.send("Operation completed !")

async def setup(bot: commands.Bot) -> None:
    await bot.add_cog(GreetingCog(bot), guild=discord.Object(id=os.getenv("GUILD_ID")))