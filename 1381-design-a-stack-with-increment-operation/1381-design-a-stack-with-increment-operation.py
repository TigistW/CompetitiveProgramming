class CustomStack:

    def __init__(self, maxSize: int):
      self.stack = ['-inf'] * maxSize

    def push(self, x: int) -> None:
      for i in range(len(self.stack)):
        if self.stack[i] == '-inf':
          self.stack[i] = x
          break
          
      
    def pop(self) -> int:
      # print(self.stack)
      val = 0
      if self.stack[0] == '-inf':
        return -1
      elif self.stack[-1] != '-inf':
          res = self.stack[-1]
          self.stack[-1] = '-inf'
          return res
      else:
        for i in range(len(self.stack)):
          if self.stack[i] != '-inf':
            val = i
          else:
            res = self.stack[val]
            self.stack[val] = '-inf'
            return res

    def increment(self, k: int, val: int) -> None:
      for i in range(min(k, len(self.stack))):
        if self.stack[i] != '-inf':
          self.stack[i] += val
      # print(self.stack)
        


# Your CustomStack object will be instantiated and called as such:
# obj = CustomStack(maxSize)
# obj.push(x)
# param_2 = obj.pop()
# obj.increment(k,val)