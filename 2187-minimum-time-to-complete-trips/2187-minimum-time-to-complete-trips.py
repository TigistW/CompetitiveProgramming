class Solution:
    def minimumTime(self, time: List[int], totalTrips: int) -> int:
        left = 1
        right = min(time) * totalTrips
        best = 0
        
        while left <= right:
            numTrip = 0
            mid = left + (right - left) // 2
            for i in time:   
                numTrip += (mid // i)
            if numTrip >= totalTrips:
                best = mid
                right = mid - 1
            else:
                left = mid + 1   
        return best