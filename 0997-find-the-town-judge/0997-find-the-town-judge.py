class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        trusted_by = {}
        trusts ={}
        
        if n==1: return 1
  
        for a, b in trust:
            trusted_by[b] = 1 + trusted_by.get(b, 0)
            trusts[a] = b

        for keys in trusted_by:
            if trusted_by[keys]== n-1 and keys not in trusts:
                return keys

        return -1