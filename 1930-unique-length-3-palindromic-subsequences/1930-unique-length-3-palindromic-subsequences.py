class Solution:
    def countPalindromicSubsequence(self, s: str) -> int:
        dicti = defaultdict(list)
        for i in range(len(s)):
            if s[i] not in dicti:
                dicti[s[i]] = [i,i]  
            else:
                dicti[s[i]][1] = i
        count = 0
        for key in dicti:
            start = dicti[key][0]
            end = dicti[key][1]
            if end - start >= 2:
                count += len(set(s[start + 1:end]))
        return count
                
        
                