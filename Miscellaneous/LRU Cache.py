class LRUCache:

    def __init__(self, capacity: int):
        self.recent_dict = dict()
        self.capacity = capacity
        self.cache = dict()
        self.updateCnt = 0

    def get(self, key: int) -> int:
        if key in self.cache:
            self.updateCnt += 1
            self.recent_dict[key] = self.updateCnt
            return self.cache[key]
        return -1

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            self.cache[key] = value
            self.updateCnt += 1
            self.recent_dict[key] = self.updateCnt
        else:
            if len(self.recent_dict) == self.capacity:
                min_key = min(self.recent_dict, key=self.recent_dict.get)
                del self.recent_dict[min_key]
                del self.cache[min_key]

            self.updateCnt += 1
            self.recent_dict[key] = self.updateCnt
            self.cache[key] = value


cache = LRUCache(2)
cache.put(1, 1)
cache.put(2, 2)
print(cache.get(1))
cache.put(3, 3)
print(cache.get(2))
cache.put(4, 4)
print(cache.get(1))
print(cache.get(3))
print(cache.get(4))
