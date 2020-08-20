import random
import time
import requests
import pandas as pd
from bs4 import BeautifulSoup
from urllib.parse import urljoin


BASE_URL = 'https://maoyan.com'


def fetch(url):
    """
    Fetch given url page by using requests and return response html text if success
    """
    user_agent = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.125 Safari/537.36'
    cookie = '__mta=210532266.1597856646388.1597856709219.1597857662901.12; uuid_n_v=v1; uuid=F50E50E0E23D11EA9E4093FE693252837CA0C6EB724249F5B2111828D7A1B702; _csrf=985048b5e3059160ef776c933c08512465d19b9070cf587b9c5768f5a4ddc007; _lxsdk_cuid=17407ad819cc8-0e8bad765cfc1b-3323767-384000-17407ad819cc8; _lxsdk=F50E50E0E23D11EA9E4093FE693252837CA0C6EB724249F5B2111828D7A1B702; mojo-uuid=05bca89a7fafaed21a6f70d22cb566ff; mojo-session-id={"id":"42f0a7841796018ad3658f182a68b1b6","time":1597856646270}; Hm_lvt_703e94591e87be68cc8da0da7cbd0be2=1597856646,1597856696,1597856709; __mta=210532266.1597856646388.1597856707790.1597856709219.11; mojo-trace-id=16; Hm_lpvt_703e94591e87be68cc8da0da7cbd0be2=1597857662; _lxsdk_s=17407ad819d-908-03e-960%7C%7C29'
    headers = {'user-agent': user_agent, 'cookie': cookie}
    try:
        res = requests.get(url, headers=headers)
        if res.status_code == 200:
            return res.text
        print("status code:", res.status_code)
    except requests.RequestException as e:
        raise e


def parse_index(url):
    """
    Parse index html and return first 10 movies' links
    :param url: index url
    :return: movies' links
    """
    res_text = fetch(url)
    soup = BeautifulSoup(res_text, 'html.parser')
    movie_list = soup.find_all('div', class_='movie-item-title', limit=10)
    for movie in movie_list:
        href = urljoin(BASE_URL, movie.find('a').get('href'))
        yield href


def parse_details(url):
    """
    Parse movie detail url and return movie data dict
    :param url: movie detail url
    :return: movie data (dict)
    """
    res_text = fetch(url)
    soup = BeautifulSoup(res_text, 'html.parser')
    movie_brief = soup.find('div', class_="movie-brief-container")
    title = movie_brief.find('h1').text
    categories = [atag.text.strip() for atag in movie_brief.find_all('a')]
    release_time = movie_brief.find_all("li")[-1].text
    data = {
        'title': title,
        'categories': categories,
        'release_time': release_time
    }
    print(data)
    return data


def save(data):
    """
    Save movie data by DataFrame
    """
    df = pd.DataFrame(data)
    df.to_csv('./movie.csv', encoding='utf-8', header=False, index=False)


def main():
    url = "https://maoyan.com/films?showType=3"
    data_list = []
    for detail in parse_index(url):
        movie = parse_details(detail)
        if random.random() < 0.5:
            time.sleep(1)
        data_list.append(movie)
    save(data_list)


if __name__ == '__main__':
    data = fetch("https://maoyan.com/films/456826")
    from lxml import etree
    selector = etree.HTML(data)
    movie_brief = selector.xpath('//div[@class="movie-brief-container"]')
    categories = movie_brief.xpath('//a/text()')
    print(categories)
    main()
