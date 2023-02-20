class Solution:
    def expressiveWords(self, s: str, words: List[str]) -> int:
        def isPossible(s, word):
            m, n = len(s), len(word)
            i, j = 0, 0
            if m<n:
                return False
            while i < m or j < n:
                if j == n:
                    l = 1
                    start = i
                    while start-1 >= 0 and s[start-1] == s[start]:
                        l += 1
                        start -= 1
                    r = 0
                    while i+1 < m and s[i] == s[i+1]:
                        r += 1
                        i += 1
                    i += 1
                    if l+r < 3:
                        return False
                    break
                if i == m and j<n:
                    return False

                if s[i] == word[j]:
                    i += 1 
                    j += 1
                    continue
                if i == 0:
                    return False
                if s[i-1]!=s[i]:
                    return False
                l = 1
                start = i
                while start-1>=0 and s[start-1] == s[start]:
                    l += 1
                    start -= 1
                r = 0
                while i+1<m and s[i] == s[i+1]:
                    r += 1
                    i += 1
                i += 1
                if l+r<3:
                    return False
            return i==m and j==n
        res = 0   
        for i, word in enumerate(words):
            if isPossible(s, word):
                res += 1
        return res