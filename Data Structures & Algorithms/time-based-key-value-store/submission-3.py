class TimeMap:

    def __init__(self):
        self.cache = defaultdict(list)

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.cache[key].append([value, timestamp])

    def get(self, key: str, timestamp: int) -> str:
        res = ""
        values = self.cache.get(key, [])

        l, r = 0, len(values) - 1
        while l <= r:
            m = l + (r - l) // 2
            if values[m][1] <= timestamp:
                res = values[m][0]
                l = m + 1
            else:
                r = m - 1

        return res
