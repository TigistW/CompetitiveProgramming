class Solution:
    def convertToTitle(self, columnNumber: int) -> str:
        ans=""
        while columnNumber:
            columnNumber -= 1
            val = chr((columnNumber % 26) + ord("A"))
            ans = val + ans
            columnNumber //= 26
        return ans
            
            