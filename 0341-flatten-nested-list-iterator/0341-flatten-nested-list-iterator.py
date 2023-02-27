# """
# This is the interface that allows for creating nested lists.
# You should not implement it, or speculate about its implementation
# """
#class NestedInteger:
#    def isInteger(self) -> bool:
#        """
#        @return True if this NestedInteger holds a single integer, rather than a nested list.
#        """
#
#    def getInteger(self) -> int:
#        """
#        @return the single integer that this NestedInteger holds, if it holds a single integer
#        Return None if this NestedInteger holds a nested list
#        """
#
#    def getList(self) -> [NestedInteger]:
#        """
#        @return the nested list that this NestedInteger holds, if it holds a nested list
#        Return None if this NestedInteger holds a single integer
#        """

class NestedIterator:
    def __init__(self, nestedList: list[NestedInteger]):
        self.ans = deque(nestedList)
    
    def next(self) -> int:
        val = self.ans.popleft()
        bl = val.getInteger()
        return bl
    
    def hasNext(self) -> bool:
        val = self.ans
        while val and not val[0].isInteger():
            num = self.ans.popleft()
            num = num.getList()
            for i in range(len(num)-1, -1, -1):
                self.ans.appendleft(num[i])
        return self.ans
    
    
    
    
    

# # Your NestedIterator object will be instantiated and called as such:
# # i, v = NestedIterator(nestedList), []
# # while i.hasNext(): v.append(i.next())