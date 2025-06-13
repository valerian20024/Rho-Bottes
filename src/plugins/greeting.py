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
        try:
            async with ctx.channel.typing():
                await asyncio.sleep(5)
            await ctx.send("Operation completed !")
        except Exception as e:
            await ctx.send(f"An error occurred: {str(e)}")
            print(f"Error: {e}")

async def setup(bot: commands.Bot) -> None:
    await bot.add_cog(GreetingCog(bot), guild=discord.Object(id=os.getenv("GUILD_ID")))