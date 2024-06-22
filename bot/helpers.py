from asyncio import gather
from copy import deepcopy

from random import sample, randint
from timeit import default_timer

from discord import utils

from bot.consts import points, threshold, refresh_interval
from bot.db_utils import load_json, update_build_id
from bot.scrapper import get_rank, get_build_id


async def draw(mid_point: float, list_ranked_summoners: list[tuple[str, int]]) -> \
        tuple[dict[str, int | list], dict[str, int | list]]:
    blue_team = {'score': 0, 'players': []}
    while blue_team['score'] < mid_point:
        random_index = randint(0, len(list_ranked_summoners) - 1)
        random_summoner = list_ranked_summoners[random_index]
        blue_team['players'].append(random_summoner[0])
        blue_team['score'] += random_summoner[1]
        a = list_ranked_summoners.pop(random_index)
        if len(blue_team.get('players')) == 4:
            comparison_value = mid_point - blue_team['score']
            elected_summoner = 0
            min_value = abs(list_ranked_summoners[0][1] - comparison_value)
            for j in range(0, len(list_ranked_summoners) - 1):
                if abs(list_ranked_summoners[j][1] - comparison_value) < min_value:
                    elected_summoner = j
                    min_value = abs(list_ranked_summoners[j][1] - comparison_value)
            blue_team['players'].append(list_ranked_summoners[elected_summoner][0])
            blue_team['score'] += list_ranked_summoners[elected_summoner][1]
            list_ranked_summoners.pop(elected_summoner)
            break
        if len(blue_team['players']) == 5:
            break
    red_team = {
        'score': mid_point * 2 - blue_team.get('score'),
        'players': [summoner[0] for summoner in list_ranked_summoners]
    }
    return blue_team, red_team
