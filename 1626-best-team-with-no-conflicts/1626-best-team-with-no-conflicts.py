class Solution:
    def bestTeamScore(self, scores: List[int], ages: List[int]) -> int:
        li = sorted(list(zip(ages, scores)))
        dp = [i[1] for i in li]
        
        for i in range(1, len(li)):
            for j in range(i):
                if li[i][1] >= li[j][1]:
                    dp[i]=max(dp[i], li[i][1]+dp[j])              
        return max(dp)