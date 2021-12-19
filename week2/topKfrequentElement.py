#https://leetcode.com/problems/top-k-frequent-elements/
class Solution:
    def topKFrequent(self, nums: List[int], k: int):
        dictt=defaultdict(int)
        listt=[]
        for i in nums:
            dictt[i]+=1        
        li=list(sorted(dictt.items(),reverse=True, key=lambda x: x[1]))
        for i in range(k):
            listt.append(li[i][0])
        return listt