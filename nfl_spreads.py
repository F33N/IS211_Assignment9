import requests
from bs4 import BeautifulSoup

url = "http://www.footballlocks.com/nfl_point_spreads.shtml"


def main():
    global spread, underdog, favorite
    response = requests.get(url)
    soup = BeautifulSoup(response.text, features='lxml')
    rows = soup.find_all('tr', class_= 'font4')

    for n, row in enumerate(rows):
        if n > 15:
            break
        cells = row.find_all("td")
        row.find_all("td")
        favorite = cells[0].find('span', title_='Favorite').text.strip()
        spread = Spread.find('span', title_='Spread').text.strip()
        underdog = Underdog.find('span', title_='Underdog').text.strip()

        print(f"{favorite} {spread} {underdog} ")


if __name__ == "__main__":
    main()