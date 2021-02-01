from rejson import Client
import time

rj = Client(host='localhost', port=6379, decode_responses=True)

times = []
start_time = time.time()

for i in range(107):
    print(i)
    start_time = time.time()
    rj.jsonget("author_" + str(i))
    elapsed_time = (time.time() - start_time)
    times.append(elapsed_time)

print("---Time elapsed---")
print(sum(times) / len(times))
