import discord
from discord.ext import commands
import csv, requests
from datetime import datetime

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

    def _mkColorNamePretty(colName: str):
        if ':' in colName:
            colName = colName.split(":")[1].title()
        return colName

    @commands.command()
    async def randColor2(self, ctx):
        colorName, colorNbStr = random.choice(list(colors.get_named_colors_mapping().items()))

        colorHex = discord.Color(value=int(colorNbStr[1:], 16))
        colorNamePretty = RandomCog._mkColorNamePretty(colorName)

        e = discord.Embed(title=colorNamePretty, color=colorHex)
        e.add_field(name="Real name", value=colorName)
        e.add_field(name="Hex value", value=colorNbStr)
        
        return await ctx.send(embed=e)

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
        with open('../data/colors.csv') as f:
            reader = csv.reader(f)
            chosenColor = random.choice(list(reader))

        emb = discord.Embed(
            title=chosenColor[1],
            description=chosenColor[0],
            color=discord.Color.from_str(chosenColor[0])
        )
        return await ctx.send(embed=emb)

    @commands.command()
    async def apod(self, ctx, day=0, month=0, year=0):
        if day not in range(1, 31) or month not in range(1, 12) or year not in range(2015, datetime.now().year + 1):
            now = datetime.now()
            nowPretty = now.strftime("%d/%m/%y")
            nowYYMMDD = now.strftime("%y%m%d")
        else:
            if month < 10:
                month = "0" + str(month)
            if day < 10:
                day = "0" + str(day)
            nowPretty = str(day) + "/" + str(month) + "/" + str(year)
            nowYYMMDD = str(year)[2:] + str(month) + str(day)

        pageURL = 'https://apod.nasa.gov/apod/ap' + nowYYMMDD + '.html'

        r = requests.get(pageURL)
        htmlCode = r.text
        imgSubStrStart = htmlCode.find('<a href="image')  # finding image url 
        imgSubStrEnd = htmlCode.find('"', imgSubStrStart + 13)  # finding next " caracter
        imageURL = 'https://apod.nasa.gov/apod/' + htmlCode[imgSubStrStart+9 : imgSubStrEnd]  # removes <a href="

        descSubStrStart = htmlCode.find('<center>\n<b>')  # should make a function for this
        descSubStrEnd = htmlCode.find('</b>', descSubStrStart)
        desc = htmlCode[descSubStrStart + 13 : descSubStrEnd]

        emb = discord.Embed(
            title="NASA APOD " + nowPretty,
            description=desc,
            color=discord.Color.blurple(),   
            url=pageURL
        )
        emb.set_image(url=imageURL)
        
        return await ctx.send(embed=emb)

async def setup(bot: commands.Bot) -> None:
    await bot.add_cog(RandomCog(bot))