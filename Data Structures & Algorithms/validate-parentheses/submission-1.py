class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        freq = {")" : "(", "}" : "{", "]" : "[" }

        for char in s:
            if char in freq:
                if stack and freq[char] == stack[-1]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(char)
        
        return len(stack) == 0