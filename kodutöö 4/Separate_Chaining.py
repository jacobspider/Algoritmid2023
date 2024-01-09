

class HashNode:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.next = None

class SeparateChainingHashTable:
    def __init__(self, capacity):
        self.capacity = capacity
        self.table = [None] * capacity

    def _hash(self, key):
        return hash(key) % self.capacity

    def insert(self, key, value):
        index = self._hash(key)
        node = self.table[index]
        if node is None:
            self.table[index] = HashNode(key, value)
            return
        prev = None
        while node is not None:
            if node.key == key:
                node.value = value
                return
            prev = node
            node = node.next
        prev.next = HashNode(key, value)

    def search(self, key):
        index = self._hash(key)
        node = self.table[index]
        while node:
            if node.key == key:
                return node.value
            node = node.next
        return None

    def delete(self, key):
        index = self._hash(key)
        node = self.table[index]
        prev = None
        while node:
            if node.key == key:
                if prev:
                    prev.next = node.next
                else:
                    self.table[index] = node.next
                return
            prev = node
            node = node.next


print("Testime räsitabelit:")
hash_table = SeparateChainingHashTable(10)
hash_table.insert("key1", "value1")
hash_table.insert("key2", "value2")
hash_table.insert("key1", "value1_updated")  
print("Sisestatud: key1, key2 ja uuendatud key1")


search_result1 = hash_table.search("key1")
search_result2 = hash_table.search("key2")
search_result3 = hash_table.search("key3")  
print(f"Otsingutulemused: key1={search_result1}, key2={search_result2}, key3={search_result3}")


hash_table.delete("key1")
search_result4 = hash_table.search("key1")
print(f"Pärast kustutamist: key1={search_result4}")



