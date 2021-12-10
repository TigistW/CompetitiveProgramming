#https://leetcode.com/problems/how-many-numbers-are-smaller-than-the-current-number/submissions/
class Solution:
    def smallerNumbersThanCurrent(self, arr):
        counter=[]
        for i in range(len(arr)):
            num=arr[i]
  
            count=0
            for j in range(len(arr)):
                if num > arr[j]:
                    count+=1
            counter.append(count)
        return counter