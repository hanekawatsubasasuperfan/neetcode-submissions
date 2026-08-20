from collections import deque
class Solution:
    def isValid(self, s: str) -> bool:
        # store )/}/] in  a queue or stack then we see the corresponding character we pop from it?
        mapping = {
            "(":")",
            "{":"}",
            "[":"]"
        }
        stack = deque([])
        for c in s:
            if c == "(" or c == "{" or c == "[":
                stack.append(mapping[c])
            elif c == "}" or c == "]" or c==")":
                if not stack:
                    return False
                temp = stack.pop()
                if temp!=c:
                    return False

        return not stack

           
            

        