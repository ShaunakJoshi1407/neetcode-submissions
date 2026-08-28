class Solution:
    def decodeString(self, s: str) -> str:
        stack = []

        for char in s:
            if char != ']':
                stack.append(char)
            else:
                substr = ""
                while stack and stack[-1] != '[':
                    substr = stack.pop() + substr
                
                stack.pop()

                value = ""
                while stack and stack[-1].isdigit():
                    value = stack.pop() + value
                
                stack.append(int(value) * substr)
        
        return "".join(stack)