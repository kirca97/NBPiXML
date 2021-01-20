import csv
import io
import redis
from rejson import Client, Path
import time

redis_client = redis.StrictRedis(host='localhost', port='6379', db=0)

rj = Client(host='localhost', port=6379, decode_responses=True)

# with io.open(r"C:\Users\Kiril\Downloads\archive\posts.csv", 'r', encoding="utf8", newline='') as posts:
#     reader_posts = csv.reader(posts, delimiter=",", quotechar='"', quoting=csv.QUOTE_ALL)
#     posts_authors = {}
#     for post in reader_posts:
#         current_key = "author_" + post[3] + ",post_" + post[0]
#         post_id = post[0]
#         posts_authors[post_id] = {
#             "author_id": post[3],
#             "comments": {}
#         }

with io.open(r"C:\Users\Kiril\Downloads\archive\comments.csv", 'r', encoding="utf8", newline='') as comments:
    reader_comments = csv.reader(comments, delimiter=",", quotechar='"', quoting=csv.QUOTE_ALL)
    start_time = time.time()
    for comment in reader_comments:
        current_comment = {
            "content": comment[2],
            "author": comment[3],
            "date": comment[4],
            "vote": comment[5]
        }
        rj.jsonset("post_" + comment[1], Path(".comments.comment_" + comment[0]), current_comment)
        # posts_authors[comment[1]]["comments"]["comment_" + comment[0]] = current_comment

# start_time = time.time()
# print(len(posts_authors['1']['comments']))
# for key in posts_authors:
#     post_id = "post_" + key
#     author_id = "author_" + posts_authors[key]["author_id"]
#     rj.jsonset(author_id, Path(".posts." + post_id + ".comments"), posts_authors[key]["comments"])


time_passed = time.time() - start_time

print("--- %s seconds ---" % time_passed)