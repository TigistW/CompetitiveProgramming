class Solution:
    def closeStrings(self, word1: str, word2: str) -> bool:
        c1 = Counter(word1)
        c2 = Counter(word2)
        if c1.keys() != c2.keys():
            return False
        
        if Counter(c1.values()) != Counter(c2.values()):
            return False
        
        return True