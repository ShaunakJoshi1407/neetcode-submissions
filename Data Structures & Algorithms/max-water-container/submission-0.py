class Solution:
    def maxArea(self, heights: List[int]) -> int:
        maxArea = float('-inf')

        l, r = 0, len(heights) - 1

        while l < r:
            area = (r - l) * min(heights[l], heights[r])
            maxArea = max(area, maxArea)
            if heights[r] > heights[l]:
                l += 1
            else:
                r -= 1

        
        return maxArea if maxArea != float('-inf') else 0