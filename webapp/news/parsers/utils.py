import requests

from webapp.db import db
from webapp.news.models import News


def get_html(url):
    headers = {
        'User=Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/106.0.0.0 Safari/537.36'
        }
    try:
        result = requests.get(url, headers=headers)
        result.raise_for_status()

        return result.text
    except (requests.RequestException, ValueError):
        print("Сетевая ошибка")
        return False


def save_news(title, url, published):
    news_exits = News.query.filter(News.url == url).count()
    if not news_exits:
        new_news = News(title=title, url=url, published=published)
        db.session.add(new_news)
        db.session.commit()
