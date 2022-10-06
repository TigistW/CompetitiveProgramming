class TimeMap:

    def __init__(self):
        self.dic = dict()
        self.dic_two = dict()
        
    def set(self, key: str, value: str, timestamp: int) -> None:
        self.dic[(timestamp,key)] = value
        if key not in self.dic_two: 
          self.dic_two[key] = []
        self.dic_two[key].append(timestamp)
    def get(self, key: str, timestamp: int) -> str:
        if key in self.dic_two:
          left = 0
          right = len(self.dic_two[key]) - 1
          best = 0
          while left <= right:
            mid = (left + right) // 2
            if self.dic_two[key][mid] > timestamp: 
              right = mid - 1
            else:
              left  = mid + 1
              best = mid
          # print("best",best)
          val = self.dic_two[key][best]
          if val > timestamp:
            return ""
          return self.dic[(val, key)]
        return ""
          
# Your TimeMap object will be instantiated and called as such:
# obj = TimeMap()
# obj.set(key,value,timestamp)
# param_2 = obj.get(key,timestamp)