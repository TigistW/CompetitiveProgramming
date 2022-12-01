class Solution:
    def halvesAreAlike(self, s: str) -> bool:
        sets = {"a", "e","i","o","u","A","E","I","O","U"}
        def count(word):
          count = 0
          for i in word:
            if i in sets:
              count += 1
          return count
        
        return count(s[:len(s)//2]) == count(s[len(s)//2:])