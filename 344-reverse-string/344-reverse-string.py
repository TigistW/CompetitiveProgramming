class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        size = len(s)
        for i in range(len(s)):
          s.append(s[size - 1 - i])
          s.pop(size - 1 - i)
        
        