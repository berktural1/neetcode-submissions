class Solution:
    def isValid(self, s: str) -> bool:


        closeToOpen = {'}': '{',
                       ']': '[',
                       ')': '(',}
        
        stack = []
        
        # we know it only consists of those 6 chars
        for c in s:

            if c not in closeToOpen:
                stack.append(c)
            elif c in closeToOpen and stack:
                #forgot how to look at last element of stack
                if closeToOpen[c] == stack[-1]: 
                    stack.pop()
                else:
                    return False
            else:
                return False
        
        return not stack






        