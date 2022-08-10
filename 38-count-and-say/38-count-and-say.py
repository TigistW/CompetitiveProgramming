class Solution:
    def countAndSay(self, n: int) -> str:
      res = "1"
      
      for i in range(n - 1):
        val = ""
        idx = 0
        while idx < len(res):
          num = 1
          while idx + 1 < len(res) and res[idx] == res[idx + 1]:
              num += 1
              idx += 1
          val += str(num) + res[idx] 
          idx += 1
        res = val
      return res



          
          