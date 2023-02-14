class Solution:
    def minimumDeletions(self, s: str) -> int:
        dlt = 0
        stack = []
        for c in s:
            if c == "a":
                if stack:
                    stack.pop()
                    dlt += 1
            else: stack.append(c)
                
        return dlt