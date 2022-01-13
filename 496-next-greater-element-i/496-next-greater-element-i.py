class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        ls= []
        dictt = {}
        result = []
        for i in nums2:
            while ls and ls[-1] < i:
                dictt[ls.pop()] = i
            ls.append(i)
        for i in nums1:
            if i in dictt:
                result.append(dictt[i])
            else:
                result.append(-1)
        return result
    
    
    
    