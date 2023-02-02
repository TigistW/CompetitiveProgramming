class Solution:
    def numberOfWays(self, s: str) -> int:
        zero_cnt, one_cnt, zerone_cnt, onezero_cnt,ans = 0,0,0,0,0
        for i in s:
            if i == "1": 
              one_cnt += 1
              zerone_cnt += zero_cnt
              ans += onezero_cnt
            else: 
              zero_cnt += 1
              onezero_cnt += one_cnt
              ans += zerone_cnt
        return ans
      