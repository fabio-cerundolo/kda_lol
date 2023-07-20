import json
import requests

def get_champion_data(champion_name):
    api_key = '	RGAPI-a8922dbc-2cff-4315-a315-63525b825c9b'
    url = f'https://euw1.api.riotgames.com/lol/static-data/v3/champions?api_key={api_key}'
    response = requests.get(url)
    data = response.json()

    if champion_name in data['data']:
        champion_data = data['data'][champion_name]
        return champion_data
    else:
        return 'Champion not found.'


def get_weekly_report(summoner_name):
    """This function will get the weekly report for the given summoner name."""

    # Get the summoner information.
    summoner_info = get_champion_data(summoner_name)

    # Get the summoner ID from the Riot API.
    url = "https://euw1.api.riotgames.com/lol/match/v5/matches/by-puuid/{0}/ids".format(summoner_info["puuid"])
    response = requests.get(url)
    if response.status_code == 200:
        match_ids = response.json()
    else:
        raise Exception("Error getting match IDs: {0}".format(response.status_code))

    # Get the match information for each match ID.
    matches = []
    for match_id in match_ids:
        url = "https://euw1.api.riotgames.com/lol/match/v5/matches/{0}".format(match_id)
        response = requests.get(url)
        if response.status_code == 200:
            matches.append(response.json())
        else:
            raise Exception("Error getting match information: {0}".format(response.status_code))

    # Get the weekly report for the summoner.
    weekly_report = {
        "wins": 0,
        "losses": 0,
        "kda": 0,
        "rank": 0,
        "plant": ""
    }
    for match in matches:
        if match["puuid"] == summoner_info["puuid"]:
            weekly_report["wins"] += match["winner"]
            weekly_report["losses"] += 1 - match["winner"]
            weekly_report["kda"] += match["kills"] + match["assists"]
            weekly_report["rank"] = match["rank"]
            weekly_report["plant"] = match["plant"]

    # Return the weekly report.
    return weekly_report

