from json import load, dump
from os.path import normpath
from timeit import default_timer

from bot.consts import data_folder


def load_json() -> dict[str, dict | float | str]:
    with open(normpath(f'{data_folder}/db.json'), 'r') as file:
        json = load(file)
        return json

