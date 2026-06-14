class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        for char in tokens:
            if (char == '+'):
                x1 = stack.pop()
                x2 = stack.pop()
                stack.append(x1+x2)
            elif (char == '-'):
                x1 = stack.pop()
                x2 = stack.pop()
                stack.append(x2 - x1)
            elif (char == '*'):
                x1 = stack.pop()
                x2 = stack.pop()
                stack.append(x1*x2)
            elif (char == '/'):
                x1 = stack.pop()
                x2 = stack.pop()
                stack.append(int(x2/x1))
            else:
                stack.append(int(char))
        return stack[0]
            
        
        