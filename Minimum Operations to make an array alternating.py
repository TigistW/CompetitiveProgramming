class Solution:
    def minimumOperations(self, nums: List[int]) -> int:
        def findKept():
            for i in dic_even:
                if dic_even[i] == max(dic_even.values()): 
                    kept_even = i
                    break
            for i in dic_odd:
                if dic_odd[i] == max(dic_odd.values()):
                    kept_odd = i
                    break
            if len(dic_even) == 1 and len(dic_even) == 1 and kept_even == kept_odd:
                return (kept_even,kept_odd)
            if kept_even == kept_odd:
                dic_even[kept_even] = 0
                dic_odd[kept_odd] = 0
                max_even = max(dic_even.values())
                max_odd = max(dic_odd.values())
                
                if max_even > max_odd:
                    for i in dic_even:
                        if dic_even[i] == max_even:
                            kept_even = i
                elif max_even < max_odd:
                    for i in dic_odd:
                        if dic_odd[i] == max_odd:
                            kept_odd = i
                else:
                    return findKept()
            return (kept_even,kept_odd)

        dic_even , dic_odd = dict() , dict()
        kept_even , kept_odd , count = 0 , 0 , 0
        lis_size = len(nums)
        if lis_size < 3:
            return 0
        for i in range(lis_size):
            if i % 2 == 0:
                if nums[i] not in dic_even:
                    dic_even[nums[i]] = 1
                else:
                    dic_even[nums[i]] += 1
            else:
                if nums[i] not in dic_odd:
                    dic_odd[nums[i]] = 1
                else:
                    dic_odd[nums[i]] += 1
                    
        kept_even,kept_odd = findKept()

        if kept_even == kept_odd:
                return lis_size // 2 
        for i in range(lis_size):
            if i % 2 == 0:
                if nums[i] != kept_even:
                    count += 1
            else:
                if nums[i] != kept_odd:
                    count += 1
        return count
            