class HashTable:
    def __init__(self, capacity):
        self.capacity = capacity
        self.arr = [[] for _ in range(capacity)]

    # remainder of ASCII value of the key string's 1st character divided by capacity
    def hash(self, key):
        return ord(key[0] % self.capacity)

    def get(self, key):
        hash_index = self.hash(key)
        for kvp in self.arr[hash_index]:
            if kvp[0] == key:
                return kvp[1]
    
    def set(self, key, value):
        hash_index = self.hash(key)
        for kvp in self.arr[hash_index]:
            if kvp[0] == key:
                kvp[1] = value
                return
    
    def remove(self, key):
        hash_index = self.hash(key)
        for i, kvp in enumerate(self.arr[hash_index]):
            if kvp[0] == key:
                self.table[hash_index].pop(i)
                return