class RandomizedCollection:

    def __init__(self):
      self.dictionary = defaultdict(list)
      self.li = []
        
    def insert(self, val: int) -> bool:
        if val not in self.dictionary:
          self.li.append(val)
          self.dictionary[val].append(len(self.li) - 1)
          return True
        
        self.li.append(val)
        self.dictionary[val].append(len(self.li) - 1)
        return False
        
    def remove(self, val: int) -> bool:
        if val not in self.dictionary:
          return False
        
        rev_idx = self.dictionary[val][-1]
        last_val = self.li[-1]
        
        last_val_idx = self.dictionary[last_val][-1]
        self.li[rev_idx], self.li[last_val_idx] = self.li[last_val_idx] , self.li[rev_idx]  
        self.li.pop()
        
        self.dictionary[last_val].pop()
        insort(self.dictionary[last_val], rev_idx)
        
        self.dictionary[val].pop()
        
        if len(self.dictionary[val]) == 0:
          del self.dictionary[val]
        
        return True
        
    def getRandom(self) -> int:
      return random.choice(self.li)
        
# Your RandomizedCollection object will be instantiated and called as such:
# obj = RandomizedCollection()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()