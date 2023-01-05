class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        points.sort()
        if points:
            ans = 1
        else:
            ans = 0
            return ans
        x,y = points[0][0],points[0][1]
        for point in points[1:]:
            x1,y1 = point
            if x<= x1 <= y:
                y = min(y1,y)
                continue
            else:
                ans += 1
                x,y = point
        return ans 