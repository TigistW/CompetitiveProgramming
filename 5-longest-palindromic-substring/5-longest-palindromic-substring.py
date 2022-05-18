class Solution:
  def longestPalindrome(self, s: str) -> str:
    if not s:
      return ''
    def outward(s,i,j):
      while i >= 0 and j < len(s):
        if s[i] != s[j]:
          break
        i -= 1
        j += 1
      return i + 1, j - 1
    indices = [0, 0]
    for i in range(len(s)):
      left, right = outward(s, i, i)
      if right - left > indices[1] - indices[0]:
        indices = left, right
      if i + 1 < len(s) and s[i] == s[i + 1]:
        left2, right2 = outward(s, i, i + 1)
        if right2 - left2 > indices[1] - indices[0]:
          indices = left2, right2
          
      # print(left,right) 
      # print(s[indices[0]:indices[1] + 1])
    return s[indices[0]:indices[1] + 1]

        