class Solution:
    def eliminateMaximum(self, dist: List[int], speed: List[int]) -> int:
        n = len(speed)
        time = [dist[i] / speed[i] for i in range(n)]
        time.sort(reverse = True)
        cur_time = 0
        mos_count  = 0
        while time and cur_time < time[-1]:
            mos_count += 1
            cur_time += 1
            time.pop()
        return mos_count
        
        
        