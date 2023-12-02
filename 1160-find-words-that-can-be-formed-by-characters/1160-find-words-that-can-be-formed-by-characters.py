class Solution:
    def countCharacters(self, words: List[str], chars: str) -> int:
        cnt = defaultdict(int)
        for c in chars:
            cnt[c] += 1
        
        summ = 0
        for word in words:
            wrd_cnt = defaultdict(int)
            for w in word:
                wrd_cnt[w] += 1
            
            valid = True
            for c, freq in wrd_cnt.items():
                if cnt[c] < freq:
                    valid = False
                    break
            
            if valid:
                summ += len(word)
            
        return summ