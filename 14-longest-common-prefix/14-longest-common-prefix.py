class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if not strs:
            return ""
        start = strs[0]
        for i in range(len(start)):
            for j in range(1, len(strs)):
                if i == len(strs[j]) or strs[j][i] != start[i]:
                    return start[:i]
        return start