class DoubleHashingHashTable:
    def __init__(self, capacity):
        self.capacity = capacity
        self.table = [None] * capacity
        self.size = 0

    def _hash1(self, key):
        return hash(key) % self.capacity

    def _hash2(self, key):
        return 1 + (hash(key) % (self.capacity - 1))

    def insert(self, key, value):
        if self.size == self.capacity:
            return "Hash table is full"
        index = self._hash1(key)
        step = self._hash2(key)
        while self.table[index] is not None:
            index = (index + step) % self.capacity
        self.table[index] = (key, value)
        self.size += 1

    def search(self, key):
        index = self._hash1(key)
        step = self._hash2(key)
        while self.table[index] is not None:
            if self.table[index][0] == key:
                return self.table[index][1]
            index = (index + step) % self.capacity
        return None

    def delete(self, key):
        index = self._hash1(key)
        step = self._hash2(key)
        while self.table[index] is not None:
            if self.table[index][0] == key:
                self.table[index] = None
                self.size -= 1
                return
            index = (index + step) % self.capacity
hash_table = DoubleHashingHashTable(10)
hash_table.insert("key1", "value1")
hash_table.insert("key2", "value2")
hash_table.insert("key3", "value3")


search_result1 = hash_table.search("key1")
search_result2 = hash_table.search("key2")
search_result3 = hash_table.search("key4")  


hash_table.delete("key2")
search_result4 = hash_table.search("key2") 