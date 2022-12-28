# class Node:
#   def __init__(self,val,next):
#     self.val = val
#     self.next = None


class MyCircularQueue:

    def __init__(self, k: int):
      
      self.stack = [math.inf for i in range(k)]
      self.head = 0
      self.tail = -1
      self.size = 0
        

    def enQueue(self, value: int) -> bool:
      if self.isFull():
        return False
      self.tail += 1
      self.tail %= len(self.stack)
      self.stack[self.tail] = value
      self.size += 1
      return True
      
    def deQueue(self) -> bool:
        if self.isEmpty():
          return False
        
        self.stack[self.head] = math.inf
        self.head += 1
        self.head %= len(self.stack)
        self.size -= 1
        return True

    def Front(self) -> int:
        if self.isEmpty():
          return -1
        return self.stack[self.head]

    def Rear(self) -> int:
        # print(self.tail)
        # print(self.stack[self.tail])
        if self.isEmpty():
          return -1
        return self.stack[self.tail]
        

    def isEmpty(self) -> bool:
        if self.size == 0:
          return True
        return False
        

    def isFull(self) -> bool:
        if self.size == len(self.stack):
          return True
        return False


# Your MyCircularQueue object will be instantiated and called as such:
# obj = MyCircularQueue(k)
# param_1 = obj.enQueue(value)
# param_2 = obj.deQueue()
# param_3 = obj.Front()
# param_4 = obj.Rear()
# param_5 = obj.isEmpty()
# param_6 = obj.isFull()