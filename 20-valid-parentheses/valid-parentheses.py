class Solution:
    def isValid(self, s: str) -> bool:
        # valid string
        # () valid
        # ()[]{} valid
        # (]) not valid
        # ([)]) not valid
        # open bracket must be closed by same type of close bracket
        # open bracket at the top of stack must be closed by the same close brac

        # if it's a closing bracket we know that the top of stack should be open
        # stack = (
        stack = []
        bracketMap = {'}':'{', ')':'(', ']':'['}

        for char in s:
            # if its a close bracket
            if char in bracketMap and len(stack) >= 1:
                if bracketMap[char] == stack[-1]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(char)
        
        if stack:
            return False
        else:
            return True
            



        