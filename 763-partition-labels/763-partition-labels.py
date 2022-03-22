class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        dic = {}
        for i, letter in enumerate(s):
            dic[letter] = i  
        start, end = 0, 0
        partitions = []
        
        for i, letter in enumerate(s):
            end = max(end, dic[letter])
            if i == end:
                partitions.append(end-start+1)
                start = end + 1
                
        return partitions