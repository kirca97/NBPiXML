import csv
import io
from rejson import Client, Path
import time

rj = Client(host='localhost', port=6379, decode_responses=True)

with io.open(r"C:\Users\Kiril\Downloads\archive\authors.csv", 'r', encoding="utf8", newline='') as authors:
    reader_authors = csv.reader(authors, delimiter=",", quotechar='"', quoting=csv.QUOTE_ALL)
    start_time = time.time()
    for author in reader_authors:
        current_author = {
            "name": author[1],
            "meibi": author[2],
            "meibix": author[3],
            "avg_words": author[4],
            "avg_words_no_stopwords": author[5],
            "posts": {}
        }
        rj.jsonset("author_" + author[0], Path.rootPath(), current_author)

print("--- %s seconds ---" % (time.time() - start_time))
