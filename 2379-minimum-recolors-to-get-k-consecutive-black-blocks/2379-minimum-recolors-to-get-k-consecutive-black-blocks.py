class Solution:
    def minimumRecolors(self, blocks: str, k: int) -> int:
        # the fixed window method will fix the issue
        left = 0
        right = left
        white_count, black_count = 0, 0
        ans = math.inf
        if k == len(blocks):
          count = Counter(list(blocks))
          return count["W"]
        
        while right < len(blocks):
          while right - left < k - 1:
            if blocks[right] == "W":
              white_count += 1
            right += 1
          else:
            if blocks[right] == "W":
              white_count += 1
            ans = min(white_count,ans)
            if blocks[left] == "W":
              white_count -= 1
            left += 1
            right += 1
        return ans
            
            
            