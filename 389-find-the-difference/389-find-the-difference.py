class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        dic = dict()
        for letter in t:
          if letter not in dic:
            dic[letter] = 1
          else:
            dic[letter] += 1
            
        for letter in s:
          if letter in dic:
            if dic[letter] > 0:
              dic[letter] -= 1
            if dic[letter] == 0:
              dic.pop(letter)
              
        for i in dic:
          return i
            
            
          
          
          
          