class Solution:
    def successfulPairs(self, spells: List[int], potions: List[int], success: int) -> List[int]:
        potions.sort()
        def BS(left, right, spell):
            best = -1
            while left <= right:
                mid = (left + right) // 2
                if potions[mid] * spell >= success:
                    best = mid
                    right = mid - 1
                else:
                    
                    left = mid + 1
            return best
        
        res = []
        for spell in spells:
            best = BS(0, len(potions) - 1, spell)
            if best != -1:
                res.append(len(potions) - best)
            else:
                res.append(0)
        return res
            
                
        