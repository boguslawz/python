import datetime
import itertools
import random
import time

class Sensor:
    def __iter__(self):
        return self
    def __next__(self):
        return random.random()

sensor = Sensor()
timestamps = iter(datetime.datetime.now, None)

# for stamp, value in itertools.islice(zip(timestamps, sensor), 10):
#     print(stamp, value)
#     time.sleep(1)

for x in timestamps:
    print(x)
    time.sleep(2)

for a in iter(sensor):
    print(a)
    time.sleep(2)