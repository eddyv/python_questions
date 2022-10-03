import typing
from collections import OrderedDict
from time import sleep, time
from typing import Tuple


class Window:
    def __init__(self, window_size: int):
        # window in seconds
        self.window_size = window_size
        # Cache is a mapping between (key) -> (value,timestamp)
        # We use an ordered dictionary here to preserve the "order" of when operations are added to the dictionary.
        # This will be important when pruning
        self.cache: typing.OrderedDict[str, Tuple[int, float]] = OrderedDict()
        self.current_running_average: int = 0

    def put(self, key, value):
        if key in self.cache:
            # update the key with a new timestamp and value
            (old_value, old_ts) = self.cache[key]
            self.current_running_average -= old_value
            self.cache.move_to_end(key)
        self.current_running_average += value
        self.cache[key] = (value, time() + window.window_size)

    # removes stale keys and reduces the running average
    def _prune(self):
        while self.cache:
            key, (value, timestamp) = next(iter(self.cache.items()))
            if timestamp < time():
                self.cache.popitem(last=False)
                self.current_running_average -= value
            else:
                break

    # Gets the most recent value for the key
    def get(self, key):
        self._prune()
        if key in self.cache:
            return self.cache[key][0]
        # key not found
        return -1

    # Gets the average for all values inside the window
    def getAverage(self):
        self._prune()
        return self.current_running_average / len(self.cache)


if __name__ == '__main__':
    window = Window(10)
    window.put("foo", 10)  # time 0
    sleep(4)
    window.put("bar", 2)  # time 4
    window.put("cbar", 3)  # time 4
    sleep(1)
    print(window.get("bar"))  # time 5, output: 2
    sleep(1)
    print(window.getAverage())  # time 6, output 6
    sleep(4)
    print(window.getAverage())  # time 6, output 6
    print(window.get("foo"))  # time 11, output: -1
    sleep(5)
    print(window.getAverage())
