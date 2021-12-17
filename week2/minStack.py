#https://leetcode.com/problems/min-stack/
class MinStack:

    def __init__(self):
        self.li=[]

    def push(self, val: int) -> None:
        self.li.append(val)

    def pop(self) -> None:
        val = self.li[-1]
        self.li=self.li[:-1]
        return val
    def top(self) -> int:
        return self.li[-1]

    def getMin(self) -> int:
        return min(self.li)


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()