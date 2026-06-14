class Solution:
    def isValid(self, s: str) -> bool:
        lookup = {
            '}': '{',
            ')' : '(',
            ']' : '[',
        }
        stack = []
        for char in s:
            if char not in lookup.keys():
                stack.append(char)
            else:
                if (len(stack) == 0):
                    return False
                if (stack[-1] != lookup[char]):
                    return False
                else:
                    stack.pop()
        return True if len(stack) == 0 else False

        