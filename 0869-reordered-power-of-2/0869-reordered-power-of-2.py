class Solution:
    def reorderedPowerOf2(self, N: int) -> bool:
        count = Counter(str(N))
        for i in range(30):
            if Counter(str(1 << i)) == count:
                return True
        return False