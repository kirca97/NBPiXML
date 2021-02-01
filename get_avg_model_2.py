from rejson import Client
import time

rj = Client(host='localhost', port=6379, decode_responses=True)

times = []

for i in range(19464):
    print(i)
    start_time = time.time()
    rj.jsonget("post_" + str(i))
    elapsed_time = (time.time() - start_time)
    times.append(elapsed_time)

print("---Time elapsed---")
print(sum(times) / len(times))
