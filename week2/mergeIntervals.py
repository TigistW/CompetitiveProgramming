#https://leetcode.com/problems/merge-intervals/

class Solution:
    def merge(self, intervals):
        length = len(intervals)
        intervals.sort()
        
        i = 0
        while (i <length-1):
            j=i+1
            if(intervals[i][1] >= intervals[j][0]):
                if(intervals[i][1] < intervals[j][1]):
                    intervals[i][1] = intervals[j][1]
                intervals.pop(j)
                i =i-1
                length=length-1
                
            i=i+1
        return intervals