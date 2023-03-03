class Solution:
    def threeConsecutiveOdds(self, arr: List[int]) -> bool:
        if len(arr) < 3:
            return False
        left = 0
        right = 2
        count = 0
        while left < len(arr) - 2:
            for i in range(left, right + 1):
                if arr[i] % 2 != 0:
                    count += 1

            if count != 3:
                left += 1
                right += 1
                count = 0
            else:
                return True
        return False
            