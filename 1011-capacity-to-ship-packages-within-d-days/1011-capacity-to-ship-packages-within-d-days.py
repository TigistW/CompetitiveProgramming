class Solution:
    
    def days(self, mid, weights):
        res = 0
        total = 0
        for i in weights:
            if total + i <= mid:
                total += i
            else:
                res += 1
                total = i
        return res + 1
    
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        low = max(weights)
        high = sum(weights)
        best  = -1
        
        while low <= high:
            mid = (low + high) // 2
            num_days = self.days(mid, weights)
            if num_days <= days:
                best = mid
                high = mid - 1
            else:
                low = mid + 1   
        return best
            
            
                
                