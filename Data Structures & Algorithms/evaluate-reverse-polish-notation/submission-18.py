class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        operators = "-+/*"
        stack = []

        for token in tokens:
            if token not in operators:
                stack.append(int(token))
            elif token == "+":
                first = stack.pop()
                second = stack.pop()

                stack.append(first + second)
            elif token == "-":
                first = stack.pop()
                second = stack.pop()

                stack.append(second - first)
            elif token == "*":
                first = stack.pop()
                second = stack.pop()

                stack.append(first * second)
            elif token == "/":
                first = stack.pop()
                second = stack.pop()

                stack.append(int(float(second / first)))
        
        return stack[0]
