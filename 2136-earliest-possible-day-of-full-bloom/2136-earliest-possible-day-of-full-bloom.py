class Flower(object):
    
    timeGrown = 0
    def __init__(self,plantTime,growTime):
        self.plantTime = plantTime
        self.growTime = growTime
        
    def __lt__(self,other):
        return self.growTime > other.growTime


class Solution:
    def earliestFullBloom(self, plantTime: List[int], growTime: List[int]) -> int:
        
        flowers = []
        for i in range(0,len(plantTime)):
            f = Flower(plantTime[i],growTime[i])
            flowers.append(f)
            
        flowers.sort()
        
        flowers[0].timeGrown = flowers[0].plantTime + flowers[0].growTime
        for i in range(1,len(flowers)):
            flowers[i].plantTime = flowers[i-1].plantTime + flowers[i].plantTime
            flowers[i].timeGrown = flowers[i].plantTime + flowers[i].growTime
            
        maxTime = 0
        for f in flowers:
            maxTime = max(maxTime,f.timeGrown)
        return maxTime