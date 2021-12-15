#https://leetcode.com/problems/find-original-array-from-doubled-array/
class Solution:
    def findOriginalArray(self, changed: List[int]) -> List[int]:
        # dictionary of counts
        counter = collections.Counter(changed)
        original = []
        #if array is odd return nothing
        if counter[0]%2 or len(changed)%2:
            return []
        #sort the array
        
        for i in range(len(changed)):
            for j in range(len(changed)):
                if changed[i]<changed[j]:
                    changed[i],changed[j]=changed[j],changed[i]
                
        for i in (changed):
            if counter[i] > 0:
                counter[i] -= 1
                if counter[i*2] > 0:
                    counter[i*2] -= 1
                    original.append(i)
                else:
                    return []
                
        return original
            
        print(counter)