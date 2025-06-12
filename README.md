# Rho-Bottes
Discord bot using [discord.py](https://discordpy.readthedocs.io/en/stable/#). Intended for personal use, but it might give inspiration or help others.
It's mainly made of simple commands for everyday use and for fun. And it's cute.

## Current capabilities
A review of all the commands the bot currently supports. Hopefully this list is up to date.

### Greeting:
  - hello: simply return a joyful hello message!

### Random:
  - apod: display the current [Astronomy Picture of the Day](https://apod.nasa.gov/apod/archivepix.html) in an embed.
  - rand: picks a float number between a minimum and a maximum.
  - randCard: picks a card from a traditional 52 [+ 2 if you want jokers] cards game.
  - randColor: picks a random color and displays it nicely in an embed.

### Utils:
  - halp: displays a custom help message.

​### NoCategory:
  - help: basic help display showing all the available commands.

## How to use it

### Development

Just like any Discord bot, you will need a token from [Discord](https://discord.com/developers/) to be able to use it. You will also need a container solution such as [Docker](https://www.docker.com/).
Put a `.env` file in the root folder with the `TOKEN` value equal to your token.

Then simply use the following to build the image:

`docker compose build`

And launch the container using:

`docker compose up [-d]` 

Stop the container using:

`docker compose down [-v]`

### Deployment on Podman
Using Podman 4.3 for deployment. 

Building the image from source (run in root folder): 

`podman build -t <name-of-image> -f Dockerfile .`

Running it as a container (not a pod):

`podman run -d --env-file <path-to-.env> rho-bottes:latest`

which should give you a container-ID. Otherwise, you can do the following to list all containers.

`podman container list --all`

Stopping / restarting it:

`podman container [stop|start] <container-ID|name>`

## TODO

- Deployment: for now it's forced to use SIGKILL to stop it for some reason. Will investigate on that and on the start/run mecanisms.


