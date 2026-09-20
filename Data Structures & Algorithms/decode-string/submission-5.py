class Solution:
    def decodeString(self, s: str) -> str:
        stack = []

        for char in s:
            if char != ']':
                stack.append(char)
            else:
                substr = ""
                while stack and stack[-1] != "[":
                    substr = stack.pop() + substr
                
                stack.pop()

                values = ""
                while stack and stack[-1].isdigit():
                    values = stack.pop() + values
                
                stack.append(int(values) * substr)
        
        return "".join(stack)