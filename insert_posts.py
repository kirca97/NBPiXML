import csv
import io
from rejson import Client, Path
import time

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
            "comments": {}
        }
        if "author_" + post[3] in authors:
            authors["author_" + post[3]]["post_" + post[0]] = current_post
        else:
            authors["author_" + post[3]] = {}
            authors["author_" + post[3]]["post_" + post[0]] = current_post

for key in authors.keys():
    rj.jsonset(key, Path(".posts"), authors.get(key))

print("--- %s seconds ---" % (time.time() - start_time))
