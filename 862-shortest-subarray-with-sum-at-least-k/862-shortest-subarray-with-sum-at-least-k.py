from typing import Deque
class Solution:
    def shortestSubarray(self, nums: List[int], k: int) -> int:
        count = -1
        sumn = [0]
        stack = [0]
        summa = 0
        for index in range(len(nums)):
            if nums[index] >= k:
                return 1
            summa += nums[index]
            sumn.append(summa)

        deq = Deque()
        temp_val = None
        for index in range(len(sumn)):
            
            if len(deq) == 0:
                deq.append(index)
            while len(deq) and sumn[index] - sumn[deq[0]] >= k:
                val = deq.popleft()
                if temp_val == None:
                    temp_val = index - val
                else:
                    temp_val = min(temp_val, index - val)
            while len(deq) and sumn[index] <= sumn[deq[-1]]:
                deq.pop()
            deq.append(index)
        return temp_val if temp_val != None else -1