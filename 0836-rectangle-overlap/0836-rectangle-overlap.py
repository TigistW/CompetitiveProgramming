class Solution:
    def isRectangleOverlap(self, rec1: List[int], rec2: List[int]) -> bool:
        left = max(rec1[0], rec2[0])
        right = min(rec1[2], rec2[2])
        top = min(rec1[3], rec2[3])
        bott = max(rec1[1], rec2[1])

        if right - left > 0 and top - bott > 0:
            return True
            
        return False