import csv
import io
import redis
from rejson import Client, Path
import time

redis_client = redis.StrictRedis(host='localhost', port='6379', db=0)

rj = Client(host='localhost', port=6379, decode_responses=True)

# with io.open(r"C:\Users\Kiril\Downloads\archive\posts.csv", 'r', encoding="utf8", newline='') as posts:
#     reader_posts = csv.reader(posts, delimiter=",", quotechar='"', quoting=csv.QUOTE_ALL)
#     posts_inlinks = {}
#     for post in reader_posts:
#         current_key = "author_" + post[3] + ",post_" + post[0]
#         post_id = post[0]
#         posts_inlinks[post_id] = {
#             "author_id": post[3],
#             "inlinks": {}
#         }

with io.open(r"C:\Users\Kiril\Downloads\archive\inlinks.csv", 'r', encoding="utf8", newline='') as inlinks:
    reader_inlinks = csv.reader(inlinks, delimiter=",", quotechar='"', quoting=csv.QUOTE_ALL)
    start_time = time.time()
    for inlink in reader_inlinks:
        current_inlink = {
            "title": inlink[2],
            "author": inlink[3],
            "date": inlink[4],
            "url": inlink[5]
        }
        rj.jsonset("post_" + inlink[1], Path(".inlinks.inlink_" + inlink[0]), current_inlink)
        # posts_inlinks[inlink[1]]["inlinks"]["inlink_" + inlink[0]] = current_inlink

# start_time = time.time()
#
# for key in posts_inlinks:
#     post_id = "post_" + key
#     author_id = "author_" + posts_inlinks[key]["author_id"]
#     rj.jsonset(author_id, Path(".posts." + post_id + ".inlinks"), posts_inlinks[key]["inlinks"])


time_passed = time.time() - start_time

print("--- %s seconds ---" % time_passed)