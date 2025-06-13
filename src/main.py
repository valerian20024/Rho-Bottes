import discord
from discord.ext import commands
import os

class RhoBottes(commands.Bot):
    def __init__(self) -> None:
        ints = discord.Intents.default()
        ints.members = False
        ints.message_content = True
        ints.presences = False
        desc = "Rho Bottes Pythoné!"
        commPref = "$"
        super().__init__(command_prefix=commPref, 
                         intents=ints,
                         description=desc)

    async def setup_hook(self) -> None:
        await self.load_extension("plugins.utils")
        await self.load_extension("plugins.greeting")
        await self.load_extension("plugins.random")
        await self.load_extension("plugins.api")
        
        await self.tree.sync(guild=discord.Object(id=os.getenv("GUILD_ID")))
        
    async def on_ready(self) -> None:
        print("Rho Bottes is online.")

bot = RhoBottes()

@bot.tree.command(guild=discord.Object(id=os.getenv("GUILD_ID")), name="slashy")
async def test_command(interaction: discord.Interaction):
    author = interaction.user
    await interaction.response.send_message(author.name)


def main():    
    # rhoBottes = RhoBottes()
    bot.run(os.getenv("TOKEN"))

if __name__=="__main__":
    main()
