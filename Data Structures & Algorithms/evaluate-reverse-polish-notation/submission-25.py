class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        operators = "-+/*"
        stack = []

        for token in tokens:
            if token not in operators:
                stack.append(int(token))
            elif token == "-":
                val1 = stack.pop()
                val2 = stack.pop()
                stack.append(val2 - val1)
            elif token == "*":
                val1 = stack.pop()
                val2 = stack.pop()
                stack.append(val1 * val2)
            elif token == "+":
                val1 = stack.pop()
                val2 = stack.pop()
                stack.append(val1 + val2)
            elif token == "/":
                val1 = stack.pop()
                val2 = stack.pop()
                stack.append(int(float(val2 / val1)))
        
        return stack[0]