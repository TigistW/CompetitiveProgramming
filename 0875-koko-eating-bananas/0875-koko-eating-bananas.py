class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        left = 1
        right = max(piles)
        best = max(piles)
        while left <= right:
            mid = (left + right) // 2
            # print(left,mid,right,best,self.hours(piles,mid))
            if self.hours(piles,mid) > h:
                left = mid + 1
            elif self.hours(piles,mid) <= h:
                best = min(best,mid)
                right = mid - 1

        return best
        
    def hours(self, piles,speed):
        count = 0
        for i in piles:
            count += math.ceil(i / speed)
        return count
      
      