class DataStream:

    def __init__(self, value: int, k: int):
      
        self.val = []
        self.left = 0
        self.right = 0
        self.value = value
        self.k = k
        self.count = defaultdict()
        
    def consec(self, num: int) -> bool:
        self.val.append(num)
        if len(self.val) <= self.k:
          if num in self.count:
            self.count[num] += 1
          else:
            self.count[num] = 1
          self.right += 1
          if self.value not in self.count:
            return False
          return self.k == self.count[self.value]
        else:
          self.count[self.val[self.left]] -= 1
          if num in self.count:
            self.count[num] += 1
          else:
            self.count[num] = 1
          self.left += 1
          self.right += 1
          if self.value not in self.count:
            return False
          return self.k == self.count[self.value]
        
# Your DataStream object will be instantiated and called as such:
# obj = DataStream(value, k)
# param_1 = obj.consec(num)