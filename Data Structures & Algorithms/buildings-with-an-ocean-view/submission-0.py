class Solution:
    def findBuildings(self, heights: List[int]) -> List[int]:
        stack = []

        for i, a in enumerate(heights):
            while stack and heights[stack[-1]] <= a:
                stack.pop()
            
            stack.append(i)
        
        return stack
