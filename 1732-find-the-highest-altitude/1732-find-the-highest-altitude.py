class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
        pref = [float(-inf)] * len(gain)
        pref[0] = gain[0]
        
        for i in range(1,len(gain)):
          pref[i] = pref[i - 1] + gain[i]
        return 0 if max(pref) < 0 else max(pref)