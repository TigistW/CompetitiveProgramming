class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        heap=[]
        for i in  range(len(nums)):
            heapq.heappush(heap,(-1*nums[i]))

        while k:
            curr = heapq.heappop(heap)
            k=k-1
        return curr * -1  

            