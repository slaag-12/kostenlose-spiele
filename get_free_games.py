import requests
import json

def get_free_games():
    url = "https://www.freegames.gg/api/giveaways"
    response = requests.get(url)
    giveaways = response.json()

    active = [game for game in giveaways if game['status'] == 'Active']

    simplified = [{
        'title': game['title'],
        'store': game['platform'],
        'url': game['url'],
        'image': game['image'],
        'endDate': game['endDate']
    } for game in active]

    with open("free_games.json", "w", encoding='utf-8') as f:
        json.dump(simplified, f, ensure_ascii=False, indent=2)

if __name__ == "__main__":
    get_free_games()
