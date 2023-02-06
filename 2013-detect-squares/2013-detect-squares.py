class DetectSquares:

    def __init__(self):
        self.dic = defaultdict(int)
        
    def add(self, point: List[int]) -> None:
        self.dic[tuple(point)] += 1
        
    def count(self, point: List[int]) -> int:
        self.cnt = 0
        x_comp, y_comp = point
        for pnt ,cnt in self.dic.items():
            i, j = pnt
            x_dis, y_dis  = fabs(x_comp - i), fabs(y_comp - j)
            if x_dis == y_dis and x_dis > 0:
                one, two = (x_comp, j), (i, y_comp)
                if one in self.dic and two in self.dic:
                    self.cnt += cnt * self.dic[one] * self.dic[two]

        return self.cnt
                    
        


# Your DetectSquares object will be instantiated and called as such:
# obj = DetectSquares()
# obj.add(point)
# param_2 = obj.count(point)