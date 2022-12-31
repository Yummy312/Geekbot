import requests
from bs4 import BeautifulSoup
from parser_films.models import ParserFather

URL = 'https://www.kinoafisha.info/online/movies/'


class ParserFilm(ParserFather):
    @staticmethod
    def __get_data(html):
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

    @classmethod
    def parsing_pages(cls, count=None):
        if count < 0:
            raise Exception('the num must be more than zero')
        conn = cls.get_html(URL)
        if conn.status_code == 200:
            films = []
            for i in range(0, count + 1):
                page = cls.get_html(URL + f"?page={i}")
                content = cls.__get_data(page.text)
                films.extend(content)
                return films
        else:
            raise Exception('Bad requests')

