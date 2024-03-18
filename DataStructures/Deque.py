# Deque ADT
# Deque() - Creates a new deque that is empty
# addFront(item) - Adds a new item to the front of the deque
# addRear(item) - Adds a new item to the rear of the deque
# removeFront() - Removes the front item from the deque
# removeRear() - Removes the rear item from the deque
# isEmpty() - Tests to see whether the deque is empty
# size() - Returns the number of items in the deque

class Deque:
    def __init__(self) -> None:
        self.items = []
    
    def addFront(self, item) -> None:
        self.items.append(item)
    
    def addRear(self,item) -> None:
        self.items.insert(0,item)
    
    def removeFront(self,item) -> None:
        self.items.pop()
    
    def removeRear(self) -> None:
        self.items.pop(0)
    
    def size(self) -> int:
        return self.items.length
    
# Next step can be to define append/insert/pop