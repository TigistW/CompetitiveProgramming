class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        
        dic = dict()
        for i in magazine:
          if i not in dic:
            dic[i] = 1
          else:
            dic[i] += 1
        # print(dic)
        
        for i in ransomNote:
          # print(dic[i])
          if i in dic:
            if dic[i] >= 1:
              dic[i] -= 1
            else:
              return False
          else:
            return False
          
        return True
            
             