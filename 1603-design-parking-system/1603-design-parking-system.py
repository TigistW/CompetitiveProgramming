class ParkingSystem:

    def __init__(self, big: int, medium: int, small: int):
        self.vals = [0, big, medium, small]
        self.added = [0, 0, 0, 0]

    def addCar(self, carType: int) -> bool:
        if self.added[carType] < self.vals[carType]:
          self.added[carType] += 1
          return True
        return False

# Your ParkingSystem object will be instantiated and called as such:
# obj = ParkingSystem(big, medium, small)
# param_1 = obj.addCar(carType)