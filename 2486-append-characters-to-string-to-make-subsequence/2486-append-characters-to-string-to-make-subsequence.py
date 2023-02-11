class Solution:
    def appendCharacters(self, s: str, t: str) -> int:
        one = 0
        two = 0
        
        while two < len(s) and one < len(t):
            if s[two] == t[one]:
                one += 1
            two += 1
        return len(t) - one