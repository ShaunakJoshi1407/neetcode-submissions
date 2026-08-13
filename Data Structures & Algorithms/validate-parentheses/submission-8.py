class Solution:
    def isValid(self, s: str) -> bool:
        stack = []

        char_map = {']': '[', '}': '{', ')': '('}

        for char in s:
            if stack and char in char_map and stack[-1] == char_map[char]:
                stack.pop()
            else:
                stack.append(char)
        
        return True if len(stack) == 0 else False