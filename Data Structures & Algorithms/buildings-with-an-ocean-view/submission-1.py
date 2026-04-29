class Solution:
    def findBuildings(self, heights: List[int]) -> List[int]:
        res = [len(heights) - 1]
        height_max_so_far = heights[-1]

        for i in range(len(heights) - 2 , - 1, -1):
            if heights[i] > height_max_so_far:
                res.append(i)
                height_max_so_far = heights[i]
        
        return res[::-1]
