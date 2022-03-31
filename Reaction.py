import time
import random

print("When I say go, you hit ENTER!")
time.sleep(1)
print("Ready??")
time.sleep(random.randint(1, 5))
print("Go!")
start = time.perf_counter()
user_input = input()
finish = time.perf_counter()
print()

timespent = finish - start
print("Your reaction time is {} seconds!".format(timespent))
