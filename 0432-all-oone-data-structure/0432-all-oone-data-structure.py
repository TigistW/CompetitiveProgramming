class AllOne:
    def __init__(self):
        self.key_count = defaultdict(int)
        self.cnt = defaultdict(set)
        
        self.max_heap = []
        self.min_heap = []
        
    def inc(self, key: str) -> None:
        old = self.key_count[key]
        if self.cnt[old]:
            self.cnt[old].remove(key)
            
        old+=1
        self.cnt[old].add(key)
        self.key_count[key]=old
        heapq.heappush(self.max_heap, -(old))
        heapq.heappush(self.min_heap, (old))   
        return
        

    def dec(self, key: str) -> None:
        old = self.key_count[key]
        self.cnt[old].remove(key)
        old -= 1
        if old == 0:
            del self.key_count[key]
            return
        
        self.cnt[old].add(key)
        self.key_count[key]=old
        heapq.heappush(self.max_heap, -(old))
        heapq.heappush(self.min_heap, (old)) 
        return

    def getMaxKey(self) -> str:
        if len(self.key_count) == 0:
            return ""
        
        while self.max_heap:
            val = -heapq.heappop(self.max_heap)
            if self.cnt[val]:
                heapq.heappush(self.max_heap, -val)
                for key in self.cnt[val]:
                    return key
        return
        

    def getMinKey(self) -> str:
        if len(self.key_count) == 0:
            return ""
        
        while self.min_heap:
            val = heapq.heappop(self.min_heap)
            if self.cnt[val]:
                heapq.heappush(self.min_heap, val)
                for key in self.cnt[val]:
                    return key
        return
        

# Your AllOne object will be instantiated and called as such:
# obj = AllOne()
# obj.inc(key)
# obj.dec(key)
# param_3 = obj.getMaxKey()
# param_4 = obj.getMinKey()