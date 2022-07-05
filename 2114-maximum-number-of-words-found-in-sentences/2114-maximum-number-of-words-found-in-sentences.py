class Solution:
    def mostWordsFound(self, sentences: List[str]) -> int:
        count = 0
        ans = 0
        
        for sent in sentences:
          sent = sent.split()
          for word in sent:
            count += 1
          ans = max(count, ans)
          count = 0
        return ans
          
          