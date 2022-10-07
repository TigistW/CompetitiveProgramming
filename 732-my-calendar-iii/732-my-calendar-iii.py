class MyCalendarThree:

    def __init__(self):
      self.maxOverlaps = 1
      self.bookings = []

    def checkOverlaps_boundryCount(self):

      lst = []
      for start, end in self.bookings:
          lst.append((start, +1))
          lst.append((end, -1))
      lst.sort()

      overlaps = 0
      for b in lst:
          overlaps += b[1]
          self.maxOverlaps = max(self.maxOverlaps, overlaps)
      return self.maxOverlaps

    def book(self, start: int, end: int) -> int: 
      self.bookings.append((start, end))
      return self.checkOverlaps_boundryCount() 

# Your MyCalendarThree object will be instantiated and called as such:
# obj = MyCalendarThree()
# param_1 = obj.book(start,end)