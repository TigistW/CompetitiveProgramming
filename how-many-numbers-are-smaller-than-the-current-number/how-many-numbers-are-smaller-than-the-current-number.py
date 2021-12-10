class Solution:
    def smallerNumbersThanCurrent(self, arr: List[int]) -> List[int]:
        counter=[]
        for i in range(len(arr)):
            num=arr[i]
  
            count=0
            for j in range(len(arr)):
                if num > arr[j]:
                    count+=1
            counter.append(count)
        return counter
      