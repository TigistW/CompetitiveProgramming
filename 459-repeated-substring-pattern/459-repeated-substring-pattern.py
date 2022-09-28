class Solution:
    def repeatedSubstringPattern(self, s: str) -> bool:
        n = len(s)
        
        for i in range(len(s) - 1):
          if s[:i + 1] * (n // len( s[:i + 1])) == s:
            return True
        return False