from collections import defaultdict
from sortedcontainers import SortedDict

class TimeMap:

    def __init__(self):
        self.mp = defaultdict(SortedDict)

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.mp[key][timestamp] = value
        

    def get(self, key: str, timestamp: int) -> str:
        timestamp_dict = self.mp[key]

        if timestamp in timestamp_dict:
            return timestamp_dict[timestamp]
        idx = timestamp_dict.bisect_left(timestamp)
        if idx > 0:
            return timestamp_dict.values()[idx-1]
        return ""