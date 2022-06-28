class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        uniques = set()
        for i in nums:
          
          if i not in uniques:
            uniques.add(i)
          else:
            return True
        return False