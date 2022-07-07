class Solution:
    def checkIfPangram(self, sentence: str) -> bool:
        sets = set()
        if len(sentence) < 26:
          return False
        for i in sentence:
          if i not in sets:
            sets.add(i)
        if len(sets) == 26:
          return True
        return False

          