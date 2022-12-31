import requests


class ParserFather:
    __headers = {
        'Accept': '*/*',
        'User-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) '
                      'Chrome/108.0.0.0 Safari/537.36 '
    }

    @classmethod
    def get_html(cls, url):
        req = requests.get(url=url, headers=cls.__headers)
        return req


