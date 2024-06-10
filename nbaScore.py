from requests import get
from pprint import PrettyPrinter
import urllib3

# Disable SSL certificate verification
urllib3.disable_warnings()

BASE_URL = "https://data.nba.net"
ALL_JSON = "/prod/v1/today.json"

printer = PrettyPrinter()

def get_links():
    response = get(BASE_URL + ALL_JSON, verify=False)
    response.raise_for_status()  # Raise an exception for HTTP errors
    try:
        data = response.json()
    except Exception as e:
        print("Error decoding JSON:", e)
        print("Response content:", response.content)
        return None
    return data['links']

def get_stats():
    data = get_links()
    if data is None:
        return
    stats = data.get('PertandinganTeamStatsLeader')
    if not stats:
        print("PertandinganTeamStatsLeader not found in response.")
        return

    response = get(BASE_URL + stats, verify=False)
    response.raise_for_status()
    try:
        stats_data = response.json()
    except Exception as e:
        print("Error decoding JSON:", e)
        print("Response content:", response.content)
        return
    
    teams = stats_data.get('league', {}).get('standard', {}).get('regularSeason', {}).get('teams', [])
    if not teams:
        print("No teams found in stats data.")
        return
    
    teams = list(filter(lambda x: x['name'] != "Team", teams))
    teams.sort(key=lambda x: int(x['ppg']['rank']))
    
    for i, team in enumerate(teams):
        name = team['name']
        nickname = team['nickname']
        ppg = team['ppg']['avg']
        print(f"{i + 1}. {name} - {nickname} - {ppg}")

get_stats()
