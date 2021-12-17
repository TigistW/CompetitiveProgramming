#https://leetcode.com/problems/implement-queue-using-stacks/
class MyQueue:
    
    def __init__(self):
        self.que=[]
    def push(self, x: int) -> None:
        self.que.append(x)
    def pop(self) -> int:
        res=self.que.pop(0)
        return res
    def peek(self) -> int:
        return self.que[0]
    def empty(self) -> bool:
        if len(self.que)==0:
            return True
        return False