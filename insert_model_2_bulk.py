import csv
import io
from rejson import Client, Path
import time

rj = Client(host='localhost', port=6379, decode_responses=True)

posts_db = {}
authors_db = {}
with io.open(r"C:\Users\Kiril\Downloads\archive\authors.csv", 'r', encoding="utf8", newline='') as authors:
    reader_authors = csv.reader(authors, delimiter=",", quotechar='"', quoting=csv.QUOTE_ALL)
    for author in reader_authors:
        current_author = {
            "name": author[1],
            "meibi": author[2],
            "meibix": author[3],
            "avg_words": author[4],
            "avg_words_no_stopwords": author[5]
        }
        authors_db[author[0]] = current_author
    print("authors_done")

with io.open(r"C:\Users\Kiril\Downloads\archive\posts.csv", 'r', encoding="utf8", newline='') as posts:
    reader_posts = csv.reader(posts, delimiter=",", quotechar='"', quoting=csv.QUOTE_ALL)
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
            "author": authors_db[post[3]]
        }
        posts_db[post[0]] = current_post
    print("posts_done")

with io.open(r"C:\Users\Kiril\Downloads\archive\comments.csv", 'r', encoding="utf8", newline='') as comments:
    reader_comments = csv.reader(comments, delimiter=",", quotechar='"', quoting=csv.QUOTE_ALL)
    for comment in reader_comments:
        current_comment = {
            "content": comment[2],
            "author": comment[3],
            "date": comment[4],
            "vote": comment[5]
        }
        posts_db[comment[1]]["comments"]["comment_" + comment[0]] = current_comment
    print("comments_done")

with io.open(r"C:\Users\Kiril\Downloads\archive\inlinks.csv", 'r', encoding="utf8", newline='') as inlinks:
    reader_inlinks = csv.reader(inlinks, delimiter=",", quotechar='"', quoting=csv.QUOTE_ALL)
    for inlink in reader_inlinks:
        current_inlink = {
            "title": inlink[2],
            "author": inlink[3],
            "date": inlink[4],
            "url": inlink[5]
        }
        posts_db[inlink[1]]["inlinks"]["inlink_" + inlink[0]] = current_inlink


start_time = time.time()

for post_key in posts_db.keys():
    current_post = posts_db[post_key]
    print(post_key)
    rj.jsonset("post_" + post_key, Path.rootPath(), current_post)


print("--- %s seconds ---" % (time.time() - start_time))
