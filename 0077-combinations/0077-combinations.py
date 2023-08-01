class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        res = []
        
        def backtrack(lst, ind):
            if len(lst) == k:
                res.append(lst)
                return
            else:
                for i in range(ind, n - k + len(lst) + 2):
                    backtrack(lst + [i], i + 1)

        for j in range(1, n - k + 2):
            backtrack([j], j + 1)

        return res    
        
                