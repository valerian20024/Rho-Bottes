import discord
from discord.ext import commands
import os

class RhoBottes(commands.Bot):
    def __init__(self) -> None:
        ints = discord.Intents.default()
        ints.members = False
        ints.message_content = True
        ints.presences = False
        desc = "Pythoned Rho Bottes!"
        commPref = "!"
        super().__init__(command_prefix=commPref, 
                         intents=ints,
                         description=desc)

    async def setup_hook(self) -> None:
        await self.load_extension("plugins.utils")
        await self.load_extension("plugins.helperfunctions")
        await self.load_extension("plugins.greeting")
        await self.load_extension("plugins.random")
        await self.tree.sync()
        
    async def on_ready(self) -> None:
        print("Rho Bottes is online.")

def main():    
    rhoBottes = RhoBottes()
    rhoBottes.run(os.getenv("TOKEN"))

if __name__=="__main__":
    main()
