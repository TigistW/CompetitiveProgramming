class Solution:
    def sumOfThree(self, num: int) -> List[int]:
        if num % 3 != 0:
          return []
        val = (num // 3) - 1
        return [val,val + 1, val + 2]