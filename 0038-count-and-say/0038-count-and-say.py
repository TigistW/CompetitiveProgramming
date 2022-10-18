class Solution:
    def countAndSay(self, n: int) -> str:
      base_case = "1"
      
      for i in range(n - 1):
        val = ""
        idx = 0
        while idx < len(base_case):
          num = 1
          while idx + 1 < len(base_case) and base_case[idx] == base_case[idx + 1]:
              num += 1
              idx += 1
          val += str(num) + base_case[idx] 
          idx += 1
        base_case = val
      return base_case



          
          