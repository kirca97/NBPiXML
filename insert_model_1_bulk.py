import csv
import io
from rejson import Client, Path
import time

rj = Client(host='localhost', port=6379, decode_responses=True)
authors_db = {}

with io.open(r"C:\Users\Kiril\Downloads\archive\authors.csv", 'r', encoding="utf8", newline='') as authors:
    reader_authors = csv.reader(authors, delimiter=",", quotechar='"', quoting=csv.QUOTE_ALL)
    for author in reader_authors:
        current_author = {
            "name": author[1],
            "meibi": author[2],
            "meibix": author[3],
            "avg_words": author[4],
            "avg_words_no_stopwords": author[5],
            "posts": {}
        }
        key = author[0]
        authors_db[key] = current_author
    print("authors_done")

with io.open(r"C:\Users\Kiril\Downloads\archive\posts.csv", 'r', encoding="utf8", newline='') as posts:
    reader_posts = csv.reader(posts, delimiter=",", quotechar='"', quoting=csv.QUOTE_ALL)
    post_authors = {}
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
            "inlinks": {}
        }
        post_authors[post[0]] = post[3]
        key_author = post[3]
        key = "post_" + post[0]
        authors_db[key_author]["posts"][key] = current_post
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
        key_author = post_authors[comment[1]]
        key_post = "post_" + comment[1]
        authors_db[key_author]["posts"][key_post]["comments"]["comment_" + comment[0]] = current_comment
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
        key_author = post_authors[inlink[1]]
        key_post = "post_" + inlink[1]
        authors_db[key_author]["posts"][key_post]["inlinks"]["inlink_" + inlink[0]] = current_inlink
    print("inlinks_done")


start_time = time.time()

for author_key in authors_db.keys():
    current_author = authors_db[author_key]
    print(author_key)
    rj.jsonset("author_" + author_key, Path.rootPath(), current_author)


print("--- %s seconds ---" % (time.time() - start_time))
