class Solution:
    def findingUsersActiveMinutes(self, logs: List[List[int]], k: int) -> List[int]:
        ans = [0] * (k + 1)
        user_logs = defaultdict(set)
        for user, time in logs:
            user_logs[user].add(time)
        
        UAMs = defaultdict(int)
        for user in user_logs:
            UAMs[user] = len(user_logs[user])

        
        for i in UAMs:
            ans[UAMs[i]] += 1
        return ans[1:]
    
        
            
        