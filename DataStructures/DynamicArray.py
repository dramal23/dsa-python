class DynamicArray:
    
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.length = 0
        self.arr = [0] * self.capacity

    # get at i-th index
    def get(self, i: int) -> int:
        return self.arr[i]

    # set at i-th index
    def set(self, i: int, n: int) -> None:
        self.arr[i] = n

    # add element in the last position of the array, if full then resize
    def pushback(self, n: int) -> None:
        if self.length == self.capacity:
            self.resize()
        
        self.arr[self.length] = n
        self.length += 1

    # remove last element in the dynamic array
    def popback(self) -> int:
        if self.length > 0:
            self.arr[self.length] -= 1

    # double capacity of dynamic array, create new array with doubled cappacity and copy content
    def resize(self) -> None:
        self.capacity = self.capacity * 2
        new_array = self.capacity * []

        for i in range(self.length):
            new_array[i] = self.arr[i]
        self.arr = new_array

    # return length of current dynamic array
    def getSize(self) -> int:
        return self.length
        
    # return capacity of self array
    def getCapacity(self) -> int:
        return self.capacity