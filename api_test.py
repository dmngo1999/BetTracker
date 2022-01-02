import requests

HOST = 'api-basketball.p.rapidapi.com'
KEY = '43e2a43011msh0ac6f45f5ac41cep121821jsneced75518a71'
url = 'https://api-basketball.p.rapidapi.com/'
headers = {
    'x-rapidapi-key': KEY,
    'x-rapidapi-host': HOST
    }

def get_standings():
    standings_url = url + "standings"

    querystring = {"league":"12","season":"2019-2020"}

    r = requests.request("GET", standings_url, headers=headers, params=querystring)

    print(r.json())

def get_game():
    games_url = url + "games"

    querystring = {"timezone":"America/Los_Angeles","season":"2021-2022","date":"2021-12-21","team":"156"}

    r = requests.request("GET", games_url, headers=headers, params=querystring)

    scores = r.json()['response'][0]['scores']

    print(scores)


def main():
    get_game()

main()
