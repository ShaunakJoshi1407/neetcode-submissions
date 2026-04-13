class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        freq = {'}' : '{', ']' : '[', ')' : '('}

        for char in s:
            if char in freq and stack and stack[-1] == freq[char]:
                stack.pop()
            else:
                stack.append(char)
        
        return True if not stack else False