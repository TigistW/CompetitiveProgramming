class Solution:
    def validateStackSequences(self, pushed: List[int], popped: List[int]) -> bool:
        stack = []
        num = 0 
        for i in pushed:
            stack.append(i)
            while stack and stack[-1] == popped[num]:
                stack.pop()
                num += 1
        return not stack
