import csv
import io
from rejson import Client, Path
import time

rj = Client(host='localhost', port=6379, decode_responses=True)

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

time_passed = time.time() - start_time

print("--- %s seconds ---" % time_passed)
