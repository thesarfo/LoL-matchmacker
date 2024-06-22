This is a Discord bot that helps create teams for League of Legends based on the players' rankings. Users may register their League of Legends summoner name and participate in team formation.

## What it can do

- Register and associate a League of Legends summoner name with a Discord user.
- Display the list of players ready to play.
- Add players to the playing list.
- Close the lobby and form balanced teams.
- Send the balanced teams and player ranks to the connected Discord server.

## Setup

1. Clone the repository.
2. Install the required dependencies using pipenv:
```shell
pipenv install
```
3. Create a new Discord bot and obtain its token from the Discord Developer Portal.
4. Create a new file named `.env` in the root directory and add the following line:
```shell
TOKEN=<your_discord_bot_token>
```
Replace `<your_discord_bot_token>` with the token obtained in step 3.

5. Run the bot using the below command:
```shell
pipenv run start
```

## Usage

Once the bot is running and connected to your Discord server, you can use the following commands to interact with it:

- `!ping`: Check if the bot is responsive.
- `!reset`: Clear the playing list.
- `!playlist`: Display the list of players ready to play.
- `!register <summoner_name>`: Register your League of Legends summoner name.
- `!play`: Add yourself to the playing list.
- `!close`: Close the lobby and form balanced teams.