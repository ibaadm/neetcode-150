class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        ops = {
            '+': lambda a, b: b + a,
            '-': lambda a, b: b - a,
            '*': lambda a, b: b * a,
            '/': lambda a, b: int(b / a)
        }
        for t in tokens:
            if t in ops:
                stack.append(ops[t](stack.pop(), stack.pop()))
            else:
                stack.append(int(t))
        return stack[0]