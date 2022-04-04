class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        s_count, res = Counter(s), 0
        for letter in s_count:
            change, start = 0, 0   
            for idx, val in enumerate(s):
                if val != letter:
                    change += 1
                while change > k:
                    if s[start] != letter:
                        change -= 1
                    start += 1
                res = max(res, idx - start + 1)
        return res            

            
            