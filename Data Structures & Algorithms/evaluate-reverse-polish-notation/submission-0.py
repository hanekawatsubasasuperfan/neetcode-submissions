class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = deque() # for storing the initial tokens
        ops = set()
        ops.add('+')
        ops.add('/')
        ops.add('-')
        ops.add('*')

        for t in tokens:
            if t not in ops:
                stack.append(int(t))
            else:
                op2 = stack.pop()
                op1 = stack.pop()
                if t == '+':
                    stack.append(int(op1+op2))
                elif t == '-':
                    stack.append(int(op1-op2))
                elif t == '*':
                    stack.append(int(op1*op2))
                else:
                    stack.append(int(op1/op2))
        return stack.pop()
