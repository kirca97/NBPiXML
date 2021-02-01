import csv
import io
from rejson import Client, Path
import time

rj = Client(host='localhost', port=6379, decode_responses=True)

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


time_passed = time.time() - start_time

print("--- %s seconds ---" % time_passed)