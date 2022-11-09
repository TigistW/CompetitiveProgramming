class StockSpanner:

    def __init__(self):
      self.stock = []

    def next(self, price: int) -> int:
      return self.count(price)
        
    def count(self, price) -> int: 
        count = 0
        while self.stock and self.stock[-1][0] <= price:
          count += self.stock.pop()[1]
        self.stock.append([price, count + 1])
        
        return count + 1
            
        

        


# Your StockSpanner object will be instantiated and called as such:
# obj = StockSpanner()
# param_1 = obj.next(price)