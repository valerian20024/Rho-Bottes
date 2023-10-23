import discord
from discord.ext import commands

#from helperfunctions import _mkColorNamePretty
import matplotlib.colors as colors
import random
import numpy as np

class RandomCog(commands.Cog):
    def __init__(self, bot: commands.Bot) -> None:
        self.bot = bot

    @commands.command()
    async def hello(self, ctx: commands.Context) -> discord.Message:
        return await ctx.send("Hello")

    @commands.command()
    async def rand(self, ctx: commands.Context, min: int, max: int):
        if min > max :
            min, max = max, min
        res = round(min + (max - min) * np.random.rand(), 3)
        return await ctx.send(f"Result is : {res}")

    def _mkColorNamePretty(colName: str):
        if ':' in colName:
            colName = colName.split(":")[1].title()
        return colName

    @commands.command()
    async def randColor(self, ctx):
        colorName, colorNbStr = random.choice(list(colors.get_named_colors_mapping().items()))

        colorHex = discord.Color(value=int(colorNbStr[1:], 16))
        colorNamePretty = RandomCog._mkColorNamePretty(colorName)

        e = discord.Embed(title=colorNamePretty, color=colorHex)
        e.add_field(name="Real name", value=colorName)
        e.add_field(name="Hex value", value=colorNbStr)
        
        return await ctx.send(embed=e)

async def setup(bot: commands.Bot) -> None:
    await bot.add_cog(RandomCog(bot))