class Solution:
    def isValid(self, s: str) -> bool:

        # brute force is O(n^2) time, O(n) space. There would be a tradeoff if strings
        # were mutable. That would make the extra space O(1).
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
        return not stack # he had True if not stack else False in the solution
        