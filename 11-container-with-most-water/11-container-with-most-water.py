class Solution:
    def maxArea(self, height: List[int]) -> int:
        lenn = len(height)
        i = 0
        j = lenn -1
        g_max = 0
        current_max = 0
        while i < j:
            current_max = min(height[i], height[j]) * (j - i)
            g_max = max(g_max, current_max)
            
            if height[i] < height[j]:
                i += 1
            else:
                j -= 1
        return g_max