class Solution:
    def stringMatching(self, words: List[str]) -> List[str]:
        def isIn(word, patt):
          if patt in word:
            return True
          return False
          
        li = set()
        for word in words:
          for word2 in words:
            if word !=  word2:
              if isIn(word, word2):
                li.add(word2)
        # print(li)
        return li
              
              
              
              