class Solution:
    def maxSatisfaction(self, satisfaction: List[int]) -> int:
        def helper(sat):
            nxt = [0] * (len(sat)+1)
            curr = [0] * (len(sat)+1)
            
            for i in range(len(sat)-1, -1, -1):
                for t in range(i, -1, -1):
                    include = sat[i] * (t+1) + nxt[t+1]
                    exclude = nxt[t]
                    curr[t] = max(include, exclude)
                nxt = curr.copy()
            
            return nxt[0]
        
        satisfaction.sort()
        return helper(satisfaction)