class Solution:
    def isPrefixOfWord(self, sentence: str, searchWord: str) -> int:
      leng = len(searchWord)
      sentence = sentence.split(' ')
      # print(sentence)
      for i, word in enumerate(sentence):
        if searchWord == word[:leng]:
          return i + 1
      return -1
