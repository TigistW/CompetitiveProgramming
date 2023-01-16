class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        intervals.append(newInterval)
        intervals.sort()
        l,r=intervals[0]
        ans=[]
        for i in range(1,len(intervals)):
            a,b=intervals[i]
            if l<=a<=r:
                l=min(a,l)
                r=max(b,r)
            else:
                ans.append([l,r])
                l=a
                r=b
        if not ans or ans[-1]!=[l,r]:ans.append([l,r])
        return ans
              
            
          
            
            