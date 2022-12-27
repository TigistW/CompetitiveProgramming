class MyLinkedList:

    def __init__(self):
        self.head = None
        self.length = 0

    def get(self, index: int) -> int:
        if index > self.length-1:
            return -1 
        current = self.head
        for i in range(index):
            current = current.next
        return current.val
    
    def addAtHead(self, val: int) -> None:
        if(self.head):
            temp = Node(val)
            temp.next = self.head
            self.head = temp
        else:
            self.head = Node(val)
        self.length += 1
        
    def addAtTail(self, val: int) -> None:
        prev = None
        current = self.head
        while(current):
            prev = current
            current = current.next
        if(prev):
            prev.next = Node(val)
        else:
            self.head = Node(val)
        self.length += 1
        
    def addAtIndex(self, index: int, val: int) -> None:
        if index == 0:
            self.addAtHead(val)
            return None
        left = self.head
        for i in range(index):
            if left and (i != index-1):
                left = left.next
            elif left and (i == index-1):
                if left.next:
                    nex = left.next
                    temp = Node(val)
                    left.next = temp
                    temp.next = nex
                else:
                    temp = Node(val)
                    left.next = temp
                self.length += 1
            elif (not left):
                break
                
    def deleteAtIndex(self, index: int) -> None:
        prev = None
        
        if self.length == 1 and index == 0:
            self.head = None
            self.length -= 1
            return None   
        current = self.head
        if current and (index==0):
            temp = self.head
            self.head = temp.next
            temp.next = None
            self.length -= 1
            return None     
        for i in range(index+1):
            if current:
                if i==index:
                    if current.next:
                        prev.next = current.next
                        current.next = None
                    else:
                        prev.next = None
                    self.length -= 1

                else:
                    prev = current
                    current = current.next
                
            else:
                break         
    def showList(self):
        current = self.head
        while(current):
            print(current.val, end=" ")
            current = current.next
        print()        
class Node:
    def __init__(self, val):
        self.val = val
        self.next = None    
# Your MyLinkedList object will be instantiated and called as such:
# obj = MyLinkedList()
# param_1 = obj.get(index)
# obj.addAtHead(val)
# obj.addAtTail(val)
# obj.addAtIndex(index,val)
# obj.deleteAtIndex(index)