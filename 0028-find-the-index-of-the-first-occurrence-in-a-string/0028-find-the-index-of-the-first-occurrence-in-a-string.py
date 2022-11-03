class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        size = len(needle)
        start = needle[0]
        for i in range(len(haystack)):
            if haystack[i] == start:
                print(haystack[i:i + size])
                if haystack[i:i + size] == needle:
                    return i
        return -1