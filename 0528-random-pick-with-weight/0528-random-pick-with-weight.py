class Solution:

    def __init__(self, w: List[int]):
      self.total = sum(w)
      self.idx = [i for i in range(len(w))]
      self.prob_weight = [w[i] / self.total for i in range(len(w))]
      
    def pickIndex(self) -> int:
        rand_idx = random.choices(self.idx, weights = self.prob_weight)
        return rand_idx[0]

# Your Solution object will be instantiated and called as such:
# obj = Solution(w)
# param_1 = obj.pickIndex()