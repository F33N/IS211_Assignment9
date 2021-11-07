import requests
from bs4 import BeautifulSoup

url = "https://www.cbssports.com/nfl/stats/player/passing/nfl/regular/qualifiers/"


def main():
    response = requests.get(url)
    soup = BeautifulSoup(response.text, features="lxml")
    rows = soup.find_all('tr', class_="TableBase-bodyTr")

    for n, row in enumerate(rows):
        if n > 19:
            break
        cells = row.find_all("td")
        player = cells[0].find('span', class_="CellPlayerName--long")
        name = player.find('a').text.strip()
        position = player.find('span', class_="CellPlayerName-position").text.strip()
        team = player.find('span', class_="CellPlayerName-team").text.strip()
        touchdowns = cells[8].text.strip()

        print(f"{name}  {position}  {team}  {touchdowns} ")

if __name__ == "__main__":
    main()