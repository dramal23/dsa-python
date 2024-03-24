class HashTable:
    def __init__(self, capacity):
        self.capacity = capacity
        self.arr = [0] * capacity

    # remainder of ASCII value of the key string's 1st character divided by capacity
    def hash(self, key):
        return ord(key[0] % self.capacity)

    def get(self, key):
        hash_index = self.hash(key)
        if self.arr[hash_index] is not None:
            return self.arr[hash_index]
    
    def set(self, key, value):
        hash_index = self.hash(key)
        self.arr[hash_index] = (key, value) 
    
    def remove(self, key):
        hash_index = self.hash(key)
        if self.table[hash_index] is not None:
            self.table[hash_index] = None