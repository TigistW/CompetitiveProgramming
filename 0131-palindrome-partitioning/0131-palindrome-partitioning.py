class Solution:
    def partition(self, s: str) -> List[List[str]]:
        temp, res = [], []
        def helper(start):
            if start == len(s):
                res.append(temp[:])
                return 
            for i in range(start, len(s)):
                if s[start:i+1] == s[start:i+1][::-1]:
                    temp.append(s[start:i+1])
                    helper(i+1)
                    temp.pop()
        helper(0)
        return res