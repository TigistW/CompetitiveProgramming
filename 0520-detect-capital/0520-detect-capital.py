class Solution:
    def detectCapitalUse(self, word: str) -> bool:
        cap_pos = set()
        for k,i in enumerate(word):
          if i.isupper():
            cap_pos.add(k)
        if len(cap_pos) == len(word) or len(cap_pos) == 0 or (len(cap_pos) == 1 and 0 in cap_pos):
          return True
        return False
          