class Solution:
    def orderlyQueue(self, s: str, k: int) -> str:
        if k == 1:
          minn = s
          for i in range(len(s)):
            minn = min(minn, s[i:] + s[:i])
          return minn
        else:
          return "".join(sorted(s))
            