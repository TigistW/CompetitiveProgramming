#https://leetcode.com/problems/find-target-indices-after-sorting-array/
class Solution:
    def targetIndices(self, arr, target: int):
        TargInd=[]
#sorting the numbers
        SortedArr=[0]*len(arr)
        counter=[0]*(max(arr)+1)
        for i in range(0,len(arr)):
            counter[arr[i]]=counter[arr[i]]+1
        for i in range(1,max(arr)+1):
            counter[i]+=counter[i-1]
            i=len(arr)-1
        while i>=0:
            SortedArr[counter[arr[i]]-1]=arr[i]
            counter[arr[i]]-=1
            i=i-1
#finding the target indices
        for i in range(len(SortedArr)):
            if target==SortedArr[i]:
                TargInd.append(i)

        return TargInd


