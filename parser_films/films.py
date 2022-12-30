import requests
from bs4 import BeautifulSoup

URL = 'https://www.kinoafisha.info/online/movies/'

headers = {
    'Accept': '*/*',
    'User-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) '
                  'Chrome/108.0.0.0 Safari/537.36 '
}


def get_html(url):
    req = requests.get(url=url, headers=headers)
    return req


def get_data(html):
    soup = BeautifulSoup(html, 'html.parser')
    items = soup.find_all('div', class_="movieList_item movieItem movieItem-grid grid_cell3")
    film_list = []
    for item in items:
        info = item.find('span', class_="movieItem_year").text.split(', ')
        film = {
            'image': item.find('source', type="image/jpeg").get('srcset'),
            'link': item.find('a').get('href'),
            'title': item.find('a', class_="movieItem_title").text,
            'genre': item.find('span', class_="movieItem_genres").text,
            'date': info[0],
            'country': "".join(info[1::]).replace(' / ', ', ')

        }
        film_list.append(film)
    return film_list


# html = get_html(URL)
# res = get_data(html.text)
# print(res)

def parsing_films(num_page):
    connect = get_html(URL)
    if connect.status_code == 200:
        films = []
        for i in range(0, num_page + 1):
            page = get_html(f"{URL}?page={i}")
            content = get_data(page.text)
            films.extend(content)
            return films
    else:
        raise Exception('Bad requests')



# print(parsing_films(3))
