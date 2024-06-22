from json import dump
from os import mkdir, getenv
from os.path import exists, normpath
from typing import Any
from discord import Client, Intents, utils
from dotenv import load_dotenv
from bot.consts import data_folder
from bot.db_utils import load_json, register_player
from bot.helpers import balance, beautify_teams


class MatchMaker(Client):
    def __init__(self, *, intents: Intents, **options: Any):
        super().__init__(intents=intents, **options)
        self.playing_list = []
        self.playing_list_ids = {}
        self.players = load_json().get('players')

    async def send_ready_list(self, message):
        output_string = 'Ready to play: \n'
        for player in enumerate(self.playing_list, start=1):
            output_string += '{}. {}\n'.format(*player) \
                if player[0] != len(self.playing_list) else '{}. {}'.format(*player)
        await message.channel.send(output_string)

    def refresh_players(self):
        self.players = load_json().get("players")

    async def on_ready(self):
        print(f"Logged on as {self.user}!")

    async def on_message(self, message):
        # we do not want the bot to reply to itself
        if message.author.id == self.user.id:
            return

        content = message.content
        author_id = str(message.author.id)
        match content.split():
            case ["!ping"]:
                await message.channel.send("pong")
            case ["!reset"]:
                self.playing_list = []
                self.playing_list_ids = {}
            case ["!playlist"]:
                await self.send_ready_list(message)
            case ["!register", *summoner]:
                summoner = " ".join(summoner)
                register_player(summoner, author_id)
                self.refresh_players()
                await message.channel.send(
                    f"Username '{summoner}' successfully registered, tied to {message.author.name}"
                )
            