import requests
import pymysql
from lxml.etree import HTML
from concurrent.futures import ThreadPoolExecutor, as_completed


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
            return res
        print("status code:", res.status_code)
    except requests.RequestException as e:
        raise e


def parse_detail(url):
    response = fetch(url)
    selector = HTML(response.text)
    ratings = selector.xpath('//span[@class="comment-info"]/span[2]/@class')
    stars = [int(rating.split()[0][-2]) for rating in ratings]
    comments = selector.xpath('//span[@class="short"]/text()')
    comment_date = selector.xpath('//span[@class="comment-time "]/text()')
    comment_date = [time.strip() for time in comment_date]
    return stars, comments, comment_date


def save(connection, stars, comments, comment_date):
    for star, comment, date in zip(stars, comments, comment_date):
        try:
            with connection.cursor() as cursor:
                sql = "INSERT INTO ratings (star, comment, comment_date) VALUES (%s, %s, %s);"
                cursor.execute(sql, (star, comment, date))
            connection.commit()
        except:
            connection.rollback()


def main():
    dbInfo = {
        'host': 'localhost',
        'port': 3306,
        'user': 'root',
        'password': '',
        'db': 'geekbang'
    }
    connection = pymysql.connect(
        host = dbInfo['host'],
        port = dbInfo['port'],
        user = dbInfo['user'],
        password = dbInfo['password'],
        db = dbInfo['db']
    )
    with ThreadPoolExecutor(max_workers=4) as executor:
        BASE_URL = f"https://movie.douban.com/subject/30128916/comments?start=%s&limit=20&status=P&sort=new_score"
        all_tasks = []
        for i in range(10):
            url = BASE_URL % (i*20)
            all_tasks.append(executor.submit(parse_detail, url))
        for future in as_completed(all_tasks):
            try:
                stars, comments, comment_date = future.result()
                save(connection, stars, comments, comment_date)
            except Exception as e:
                print(e)
    
    connection.close()


if __name__ == "__main__":
    main()
