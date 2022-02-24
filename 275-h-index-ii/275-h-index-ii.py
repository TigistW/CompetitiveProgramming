class Solution:
    def hIndex(self, citations: List[int]) -> int:
        N = len(citations)
        def bs(target):
            
            best, lo, hi = N, 0, N-1
            while lo <= hi:
                mid =  lo + (hi-lo)//2
                
                if citations[mid] < target:
                    lo = mid + 1
                else:
                    best = mid
                    hi = mid - 1
                    
            if N-best >= target:
                return True
            return False
        lo, hi, best = 0, N, 0
        while lo <= hi:
            mid = lo + (hi-lo)//2
            if bs(mid):
                best = mid
                lo = mid+1
            else:
                hi = mid-1
        return best
