class Solution:
    def maximumBags(self, capacity: List[int], rocks: List[int], additionalRocks: int) -> int:
        diff = []
        
        # find the number of rocks needed to fill a bag
        for i in range(len(capacity)):
          diff.append(capacity[i] - rocks[i])
        diff.sort()
        
        '''
        try to fill the bags that need smalll additional rock requirements while counting the number of bags that reached max capacity
        '''
        count = 0
        for i in range(len(diff)):
          if diff[i] != 0:
            temp = diff[i]
            if additionalRocks >= diff[i]:
              diff[i] = 0
              count += 1
            else:
              diff[i] -= additionalRocks
            additionalRocks -= temp
          else:
            count += 1
        return count
            