class Solution:
    def buildArray(self, target: List[int], n: int) -> List[str]:
        elem = set(target)
        array = []
        count = 0
        for i in range(1,n + 1):
          if count == len(target):
            break
          array.append("Push")
          count += 1
          
          if i not in elem:
            array.append("Pop")
            count -= 1
        return array
            
            
          
          