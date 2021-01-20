import csv
import io
import redis
from rejson import Client, Path
import time

redis_client = redis.StrictRedis(host='localhost', port='6379', db=0)

rj = Client(host='localhost', port=6379, decode_responses=True)

with io.open(r"C:\Users\Kiril\Downloads\archive\posts.csv", 'r', encoding="utf8", newline='') as posts:
    reader_posts = csv.reader(posts, delimiter=",", quotechar='"', quoting=csv.QUOTE_ALL)
    authors = {}
    start_time = time.time()
    for post in reader_posts:
        current_post = {
            "title": post[1],
            "comments_number": post[4],
            "content": post[5],
            "url": post[6],
            "date": post[7],
            "retrieved_links_number": post[8],
            "retrieved_comments_number": post[9],
            "comments": {},
            "inlinks": {},
            "author": {}
        }
        rj.jsonset("post_" + post[0], Path.rootPath(), current_post)

print("--- %s seconds ---" % (time.time() - start_time))
