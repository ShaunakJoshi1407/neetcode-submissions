class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        operators = "-+/*"
        stack = []

        for char in tokens:
            if char not in operators:
                stack.append(int(char))
            elif char == "+":
                val1 = stack.pop()
                val2 = stack.pop()
                stack.append(val1 + val2)
            elif char == "-":
                val1 = stack.pop()
                val2 = stack.pop()
                stack.append(val2 - val1)
            elif char == "*":
                val1 = stack.pop()
                val2 = stack.pop()
                stack.append(val1 * val2)
            elif char == "/":
                val1 = stack.pop()
                val2 = stack.pop()
                stack.append(int(val2 / val1))
        
        return stack[0]