class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        operators = "+-*/"
        for char in tokens:
            if char not in operators:
                stack.append(int(char))
            elif char == "+":
                stack.append(stack.pop() + stack.pop())
            elif char == "-":
                num2 = stack.pop()
                num1 = stack.pop()
                stack.append(num1 - num2)
            elif char == "*":
                stack.append(stack.pop() * stack.pop())
            elif char == "/":
                num2 = stack.pop()
                num1 = stack.pop()
                stack.append(int(num1 / num2))
        return stack[0]