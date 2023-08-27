import time

start_time = time.time()

sum([i**2 for i in range(1,10**8)])

end_time = time.time()

elapsed_time = end_time - start_time

print(elapsed_time)