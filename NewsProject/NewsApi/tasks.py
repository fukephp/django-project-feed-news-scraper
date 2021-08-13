from .models import Article
from .serializers import ArticleSerializer
import feedparser, datetime

from celery import shared_task

#app = Celery('tasks', backend='db+postgresql://postgres:root@127.0.0.1/postgres', broker='amqps://dyfzvfrn:PBew9WMIBbwsXoN7tz1wOCQdVxmEOmO3@cow.rmq2.cloudamqp.com/dyfzvfrn',)

@shared_task
def get_and_store_news(args):
    feeds = feedparser.parse("https://feeds.finance.yahoo.com/rss/2.0/headline?s="+args+"&region=US&lang=en-US")
    news = feeds.entries
    for item in news:

        if Article.objects.filter(title=item.title).count() > 0:
            continue
        
        published_date_tp = datetime.datetime.strptime(item.published, "%a, %d %b %Y %H:%M:%S %z").timestamp()
        item_data = {
            "title": item.title,
            "description": item.summary,
            "link": item.link,
            "symbol": args,
            "published": datetime.datetime.fromtimestamp(published_date_tp)
        }
        serializer = ArticleSerializer(data=item_data)
        
        if serializer.is_valid():
            serializer.save()
            print("Data stored success:")
            print(serializer.data)
        else:
            print("Data stored failed:")
            print(serializer.errors)

    message = "Work is finished!"
    print(message)
    return True