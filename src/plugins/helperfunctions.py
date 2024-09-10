from discord.ext import commands

def mkColorNamePretty(colName: str):
        if ':' in colName:
            colName = colName.split(":")[1].title()
        return colName

async def setup(bot: commands.Bot):
    pass