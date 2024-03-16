class ListNode:
    def __init__(self, val:int, node = None):
        self.val = val
        self.next = node

class SinglyLinkedList:
    def __init__(self):
        self.head = ListNode(-1)
        self.tail = self.head
    
    def getNodeValueAtWantedIndex(self, index: int) -> int:
        curr = self.head.next
        i = 0
        while curr:
            if i == index:
                return curr.val
            i += 1
            curr = curr.next
        return -1

    def insertNodeAtHead(self, val: int) -> None:
        new_node = ListNode(val)
        new_node.next = self.head.next
        self.head.next = new_node.next
        if not new_node.next: #if self.head.next is empty
            self.tail = new_node

    def insertNodeAtTail(self, val: int) -> None:
        new_node = ListNode(val)
        new_node.next = self.tail.next
        self.tail = new_node.next

    def removeNodeAtWantedIndex(self, index: int) -> bool:
        i = 0
        curr = self.head
        while i < index and curr:
            i += 1
            curr = curr.next
        
        if curr and curr.next:
            if curr.next == self.tail:
                self.tail = curr
            curr.next = curr.next.next
            return True
        return False
    
    def getValues(self) -> list[int]:
        curr = self.head.next
        res = []
        while curr:
            res.append(curr.val)
            curr = curr.next
        return res