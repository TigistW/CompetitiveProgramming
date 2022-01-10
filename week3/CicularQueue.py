#https://leetcode.com/problems/design-circular-deque/
class MyCircularDeque:

    def __init__(self, k: int):
        self.begin = []
        self.end = []
        self.k = k

    def insertFront(self, value: int) -> bool:
        if self.isFull():
            return False

        self.begin.append(value)
        self.end = self.begin[::-1]
        return True

    def insertLast(self, value: int) -> bool:
        if self.isFull():
            return False

        self.end.append(value)
        self.begin = self.end[::-1]
        return True

    def deleteFront(self) -> bool:
        if self.isEmpty():
            return False

        self.begin.pop()
        self.end = self.begin[::-1]
        return True

    def deleteLast(self) -> bool:
        if self.isEmpty():
            return False

        self.end.pop()
        self.begin = self.end[::-1]
        return True

    def getFront(self) -> int:
        if self.isEmpty():
            return -1
        return self.begin[-1]

    def getRear(self) -> int:
        if self.isEmpty():
            return -1
        return self.end[-1]

    def isEmpty(self) -> bool:
        return len(self.begin) == 0

    def isFull(self) -> bool:
        return len(self.begin) == self.k


# Your MyCircularDeque object will be instantiated and called as such:
# obj = MyCircularDeque(k)
# param_1 = obj.insertFront(value)
# param_2 = obj.insertLast(value)
# param_3 = obj.deleteFront()
# param_4 = obj.deleteLast()
# param_5 = obj.getFront()
# param_6 = obj.getRear()
# param_7 = obj.isEmpty()
# param_8 = obj.isFull()
