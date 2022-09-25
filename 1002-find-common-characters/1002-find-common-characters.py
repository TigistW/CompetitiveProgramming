class Solution:
    def commonChars(self, words: List[str]) -> List[str]:
        comm  = list(words[0])
        
        for word in words:
          word = list(word)
          common = []
          for letter in comm:
            if letter in word:
              common.append(letter)
              word.remove(letter)
              
          comm = common
        return comm
              
          