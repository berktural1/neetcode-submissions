class Solution:
    def isValid(self, s: str) -> bool:

        # O(n) time and extra space complexity
        # other solutions: can't think of one within 2 mins

        # set # of chars -> dict close to open

        close_to_open = {
            '}': '{',
            ']': '[',
            ')': '(',
        }
        
        # base case of length 1 -> always false

        # use a stack to keep track of closed pairs cleanly
        seen = []

        for c in s:

            if c in close_to_open and not seen:
                return False
            elif c in close_to_open and seen:          
                # now check if it is the right char
                if close_to_open[c] == seen[-1]:
                    seen.pop()
                else:
                    return False
            
            else:
                seen.append(c)

        # way we implemented, seen has to be empty if valid
        return not seen
