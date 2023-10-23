import discord
from discord.ext import commands
import os, dotenv

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
        await self.load_extension("plugins.random")
        await self.load_extension("plugins.utils")
        await self.load_extension("plugins.helperfunctions")
        await self.tree.sync()
        
    async def on_ready(self) -> None:
        print("Rho Bottes is online.")

def main() -> None:
    dotenv.load_dotenv()
    TOKEN = os.getenv("TOKEN")
    
    if TOKEN is None:
        raise ValueError("TOKEN is not defined.")

    rhoBottes = RhoBottes()
    rhoBottes.run(token=TOKEN)
        
if __name__=="__main__":
    main()    
