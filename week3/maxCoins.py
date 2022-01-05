#https://leetcode.com/problems/maximum-number-of-coins-you-can-get/
class Solution:
    def maxCoins(self, piles: List[int]) -> int:
        coins = 0
        piles.sort()
        for i in range(len(piles)//3):
            coins += piles[-2]
            piles = piles[1:-2]
        return coins