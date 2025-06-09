import discord
from discord.ext import commands

class GreetingCog(commands.Cog):
    def __init__(self, bot: commands.Bot) -> None:
        self.bot = bot

    @commands.command()
    async def hello(self, ctx: commands.Context) -> discord.Message:
        return await ctx.send("Hello 👋")
    
async def setup(bot: commands.Bot) -> None:
    await bot.add_cog(GreetingCog(bot))