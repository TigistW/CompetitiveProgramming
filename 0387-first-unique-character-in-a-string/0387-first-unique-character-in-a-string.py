class Solution:
    def firstUniqChar(self, s: str) -> int:
        cnt = Counter(s)
        for idx, i in enumerate(s):
            if cnt[i] == 1:
                return idx
        return -1