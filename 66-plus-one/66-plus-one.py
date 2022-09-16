class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        num = 0
        for i in range(len(digits) - 1,-1,-1):
          if i == 0:
            digits[len(digits) - 1] = digits[len(digits) - 1] + 1
          num += ((10 ** i) * digits[len(digits) - 1 - i])
        return list(str(num))
          