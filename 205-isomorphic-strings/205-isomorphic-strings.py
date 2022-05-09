class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        # print(*map(s.index, s))
        # print(*map(t.index, t))
        
        if [*map(s.index, s)] == [*map(t.index, t)]:
            return True
        return False
        
            
            