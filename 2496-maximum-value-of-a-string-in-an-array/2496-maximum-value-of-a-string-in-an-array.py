class Solution:
    def maximumValue(self, strs: List[str]) -> int:
        maxx = 0
        for i in range(len(strs)):
            if strs[i].isdigit():
                maxx = max(int(strs[i]), maxx)
            else:
                 maxx = max(len(strs[i]), maxx)
        return maxx
                