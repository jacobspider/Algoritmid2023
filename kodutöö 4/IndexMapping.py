class IndexMapping:
    def __init__(self, max_value):
        self.max_value = max_value
        self.map = [False] * (max_value + 1)

    def insert(self, item):
        if 0 <= item <= self.max_value:
            self.map[item] = True

    def search(self, item):
        return 0 <= item <= self.max_value and self.map[item]

    def delete(self, item):
        if 0 <= item <= self.max_value:
            self.map[item] = False


index_map = IndexMapping(100)  
index_map.insert(10)
index_map.insert(20)
print(index_map.search(10))  
print(index_map.search(30))  
index_map.delete(10)
print(index_map.search(10))  
