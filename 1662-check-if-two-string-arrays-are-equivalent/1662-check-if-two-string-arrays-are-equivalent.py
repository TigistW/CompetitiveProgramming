class Solution:
    def arrayStringsAreEqual(self, word1: List[str], word2: List[str]) -> bool:
        word_one = ""
        word_two = ""
        
        for i in word1:
          word_one += i
        for i in word2:
          word_two += i
          
        return word_one == word_two