class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        stack = []

        for char in asteroids:
            while stack and char < 0 and stack[-1] > 0:
                diff = char + stack[-1]

                if diff > 0:
                    char = 0
                elif diff < 0:
                    stack.pop()
                else:
                    char = 0
                    stack.pop()
            
            if char:
                stack.append(char)
        
        return stack