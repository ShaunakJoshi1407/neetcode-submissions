class Solution:
    def maxArea(self, heights: List[int]) -> int:
        l, r = 0, len(heights) - 1
        max_area = float('-inf')

        while l < r:
            area = (r - l) * min(heights[r], heights[l])
            max_area = max(max_area, area)

            if heights[r] < heights[l]:
                r -= 1
            else:
                l += 1
            

        return max_area if max_area != float('-inf') else 0