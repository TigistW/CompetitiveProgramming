class Solution:
    def finalValueAfterOperations(self, operations: List[str]) -> int:
        value = 0
        for i in operations:
          
          if i == "--X" or i == "X--":
            value -= 1
            
          if i == "++X" or i == "X++":
            value += 1
            
        return value
            
          