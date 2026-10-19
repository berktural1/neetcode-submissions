class Solution:
    def isValid(self, s: str) -> bool:

        # brute force is O(n^2) time, O(1) space. tradeoff there with the following
        # stack solution being faster but taking more space.
        stack = []
        #print(bool(stack))
        closeToOpen = {')': '(',
                       ']': '[',
                       '}': '{'}
        
        for c in s: # iterate through the entire string
            
            if c in closeToOpen:
                if stack and closeToOpen[c] == stack[-1]:
                    stack.pop()
                else:
                    return False   
            else:
                stack.append(c)           

        # want the list ot be empty at the end so, return True if it is
        return True if not stack else False
        