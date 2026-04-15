class Solution:
    def isValid(self, s: str) -> bool:
        stack =[]
        freq = {'}' : '{', ']' : '[', ')' : '('}

        for char in s:
            if stack and char in freq and freq[char] == stack[-1]:
                stack.pop()
            else:
                stack.append(char)

        return True if len(stack) == 0 else False    
