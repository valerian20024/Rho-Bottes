import discord
from discord.ext import commands
import csv, requests
from datetime import datetime

import re
import os
import matplotlib.colors as colors
import random
import numpy as np

class RandomCog(commands.Cog):
    def __init__(self, bot: commands.Bot) -> None:
        self.bot = bot

    @commands.command()
    async def rand(self, ctx: commands.Context, min: int, max: int):
        if min > max :
            min, max = max, min
        res = round(min + (max - min) * np.random.rand(), 3)
        return await ctx.send(f"Result is : {res}")

    @commands.command()
    async def randCard(self, ctx, jokers=False):
        if jokers:
            deckSize = 54
        else:
            deckSize = 52
        value = np.random.randint(1, deckSize + 1)
        
        if jokers and value > 52:
            return await ctx.send("Joker \uD83C\uDCBF")
        else:
            q, r = divmod(value, 13)
            color = ("Heart \u2661", "Spade \u2664",
                     "Diamond \u2662", "Club \u2667")[q]
            v = str(r) if r <= 10 else ("Jack", "Queen", "King")[r - 11]
            
        return await ctx.send("\uD83C\uDCA0 " + v + " of " + color)
    
    @commands.command()
    async def randColor(self, ctx):
        # todo: use an environment variable for the path
        with open('/home/app/data/colors.csv') as f:
            reader = csv.reader(f)
            chosenColor = random.choice(list(reader))

        emb = discord.Embed(
            title=chosenColor[1],
            description=chosenColor[0],
            color=discord.Color.from_str(chosenColor[0])
        )
        return await ctx.send(embed=emb)

async def setup(bot: commands.Bot) -> None:
    await bot.add_cog(RandomCog(bot))