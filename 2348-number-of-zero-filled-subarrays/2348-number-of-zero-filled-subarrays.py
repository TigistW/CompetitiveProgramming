class Solution:
    def zeroFilledSubarray(self, nums: List[int]) -> int:
        lst = []
        left = 0
        right = 0
        cnt, ans = 0, 0
        while right < len(nums):
            if nums[right] == 0:
                cnt += 1  
            else:
                lst.append(cnt)
                cnt = 0
                left = right
            right += 1
        if cnt:
            lst.append(cnt)
            
        for i in lst:
            ans += ((i ** 2) + i)/2
        return int(ans)
            
        