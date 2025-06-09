import discord
from discord.ext import commands
import requests
from datetime import datetime

import re
import os


class ApiCog(commands.Cog):
    def __init__(self, bot: commands.Bot) -> None:
        self.bot = bot

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
    
    @commands.command()
    async def chat(self, ctx, query="Bonjour"):
        try:
            API_KEY = os.getenv("OPEN_WEBUI_API_KEY")
            API_URL = os.getenv("OPEN_WEBUI_URL")

            headers = {
                'Authorization': f'Bearer {API_KEY}',
                'Content-Type': 'application/json'
            }
            data = {
                "model": os.getenv("OPEN_WEBUI_MODEL"),
                "messages": [
                    {
                    "role": "user",
                    "content": query
                    }
                ]
            }

            response = requests.post(API_URL, headers=headers, json=data)
            print(f"Response status code: {response.status_code}")

            answer = response.json()['choices'][0]['message']['content']
            # todo: remove only if there is a <think></think>. Look inside the answer to get the model caracteristics
            reply = re.sub(r'<think>.*?</think>\n*', '', answer, flags=re.DOTALL)

            return await ctx.send(reply)
        except Exception as e:
            log = "Impossible to connect to the API: " + str(e) 
            print(log)
            return await ctx.send(log)
        
async def setup(bot: commands.Bot) -> None:
    await bot.add_cog(ApiCog(bot))