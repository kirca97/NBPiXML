import csv
import io
from rejson import Client, Path
import time

rj = Client(host='localhost', port=6379, decode_responses=True)

with io.open(r"C:\Users\Kiril\Downloads\archive\posts.csv", 'r', encoding="utf8", newline='') as posts:
    reader_posts = csv.reader(posts, delimiter=",", quotechar='"', quoting=csv.QUOTE_ALL)
    post_author = {}
    for post in reader_posts:
        author_id = post[3]
        post_id = post[0]
        if author_id in post_author.keys():
            post_author[author_id].append(post_id)
        else:
            post_author[author_id] = []
            post_author[author_id].append(post_id)

with io.open(r"C:\Users\Kiril\Downloads\archive\authors.csv", 'r', encoding="utf8", newline='') as authors:
    reader_authors = csv.reader(authors, delimiter=",", quotechar='"', quoting=csv.QUOTE_ALL)
    start_time = time.time()
    for author in reader_authors:
        current_author = {
            "name": author[1],
            "meibi": author[2],
            "meibix": author[3],
            "avg_words": author[4],
            "avg_words_no_stopwords": author[5]
        }

        for post_id in post_author[author[0]]:
            rj.jsonset("post_" + post_id, Path(".author"), current_author)

print("--- %s seconds ---" % (time.time() - start_time))
