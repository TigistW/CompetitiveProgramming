class Solution:
    def reverseWords(self, s: str) -> str:
        swapped = [0] * len(s)
        
        for i in range((len(s) // 2)+1):
          swapped[i] = s[len(s) - 1 - i]
          swapped[len(s) - 1 - i] = s[i]

        word = "".join(swapped)
        word = word.split(" ")
        word = word[::-1]
        return " ".join(word)
          
          