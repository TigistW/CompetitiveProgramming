class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.k=k
        self.heap=nums
        heapq.heapify(self.heap)
        # print(self.heap,self)
        n=len(self.heap)
        while n>k:
            heapq.heappop(self.heap)
            n=len(self.heap) 
    
    def add(self, val: int) -> int:
        n=len(self.heap)
        if n<self.k:
            heapq.heappush(self.heap,val)
        elif val>self.heap[0]:
            # print(self.heap[0])
            heapq.heappush(self.heap,val)
            heapq.heappop(self.heap)
                    
        # return heapq.heappop(self.heap)
        return self.heap[0]
    
# Your KthLargest object will be instantiated and called as such:
# obj = KthLargest(k, nums)
# param_1 = obj.add(val)