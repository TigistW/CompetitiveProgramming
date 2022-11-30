class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        char_freq = {}
        vals = set()
        for i in range(len(arr)):
            char_freq[arr[i]] = 1 + char_freq.get(arr[i], 0)
            
        for v in char_freq.values():
            if v in vals:
                return False
            vals.add(v)
        return True