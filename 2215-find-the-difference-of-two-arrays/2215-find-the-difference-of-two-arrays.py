class Solution:
    def findDifference(self, nums1: List[int], nums2: List[int]) -> List[List[int]]:
        set1 = set()
        set2 = set()
        
        first = len(set1)
        second = len(set2)

        arr1 = []
        arr2 = []
        arr = [[],[]]
        for i in range(len(nums1)):
            set1.add(nums1[i])
            
        for i in range(len(nums2)):
            set2.add(nums2[i])
        print(set1,set2)
        
        for i in set1:
            if i not in set2: 
                arr[0].append(i) 
        for i in set2:
            if i not in set1: 
                arr[1].append(i) 

        return arr
        