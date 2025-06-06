# Rho-Bottes
Discord bot using [discord.py](https://discordpy.readthedocs.io/en/stable/#). Intended for personal use, but it might give inspiration or help others.
It's mainly made of simple commands for everyday use and for fun. And it's cute.

## Current capabilities
A review of all the commands the bot currently supports. Hopefully this list is up to date.

### Greeting:
  hello: simply return a joyful hello message!

### Random:
  apod: display the current [Astronomy Picture of the Day](https://apod.nasa.gov/apod/archivepix.html) in an embed.
  rand: picks a float number between a minimum and a maximum.
  randCard: picks a card from a traditional 52 [+ 2 if you want jokers] cards game.
  randColor: picks a random color and displays it nicely in an embed.

### Utils:
  halp: displays a custom help message.

​### NoCategory:
  help: basic help display showing all the available commands.

## How to use it
Just like any Discord bot, you will need a token from [Discord](https://discord.com/developers/) to be able to use it. You will also need a container solution such as [Docker](https://www.docker.com/).
Put a `.env` file in the root folder with the `TOKEN` value equal to your token.

Then simply use the following to build the image:

`docker compose build`

And launch the container using:

`docker compose up [-d]` 
