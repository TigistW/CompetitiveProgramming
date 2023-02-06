class Solution:
    def prefixCount(self, words: List[str], pref: str) -> int:
        length = len(pref)
        count = 0
        for i in range(len(words)):
            if len(words[i]) < length:
                continue
            else:
                if words[i][:length] == pref:
                    count += 1
        return count
                    
        
            