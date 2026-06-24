class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        for t in tokens:
            if t == '+':
                stack.append(stack.pop() + stack.pop())
            elif t == '-':
                subtrahend = stack.pop()
                minuend = stack.pop()
                stack.append(minuend - subtrahend)
            elif t == '*':
                stack.append(stack.pop() * stack.pop())
            elif t == '/':
                divisor = stack.pop()
                dividend = stack.pop()
                stack.append(int(dividend / divisor))
            else:
                stack.append(int(t))
            print(stack)
        return stack[0]