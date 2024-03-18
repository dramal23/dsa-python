# Queue ADT
# Queue() - creates a new queue that is empty
# enqueue(item) - adds a new item to the rear of the queue
# dequeue() - removes the front item from the queue
# isEmpty() - tests to see whether the queue is empty
# size() - returns the number of items in the queue

class Queue:
    def __init__(self) -> None:
        self.items = []
    
    def enqueue(self,item) -> None:
        self.items.insert(0,item)
    
    def dequeue(self) -> None:
        self.items.pop()
    
    def isEmpty(self) -> None:
        return self.items == []
    
    def size(self) -> int:
        return self.items.length