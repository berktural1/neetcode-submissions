class Solution:
    def isPalindrome(self, s: str) -> bool:

        # first thought: remove non alphanum -> sort -> check equality

        # base case: if len==1 -> palindrome
        # case-insensitive -> change all to be upper/lower

        # each char has an integer value

        # a better way than first thought which is O(nlogn) is:
        
        # use 2 pointers to go from start and back of array moving in
        # when both are pointing at an alphanum, check equality

        if len(s) == 1 and s.isalnum():
            return True
        
        i = 0
        j = len(s) - 1 # is this right -> yes

        s = s.upper()
        print(s)

        # isalnum()

        while i < j:

             if s[i].isalnum() and s[j].isalnum():
                if s[i] != s[j]:
                    return False
                else:
                    i,j = i+1, j-1
            
             if not s[i].isalnum():
                i += 1

             if not s[j].isalnum():
                j -= 1
        
        return True


        
        