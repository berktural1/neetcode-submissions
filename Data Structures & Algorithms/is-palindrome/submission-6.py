class Solution:
    def isPalindrome(self, s: str) -> bool:


        # case sensitive -> change all inputs to be upper/lower
        # only printable ASCII chars, so finite amount
        # s is between 1 and 1000 so ideal solution O(nlogn) or better 
        # I would assume

        # option: sort then check equality -> WRONG ACTUALLY
        # O(nlogn) time, O(1) extra space, depending on sort algo

        # better solution: 2 pointers traversing inwards from
        # either side checking equality at each position
        # O(n) time, O(1) extra space

        s = s.upper()
        #print(s)

        # only check equality for alphanumeric characters
        # check if ord is between 0 and Z
        # print(ord('0'))
        # print(ord('9'))
        # print(ord('A'))
        # print(ord('Z'))

        l = 0
        r = len(s) - 1

        while l <= r:

            # print(l, self.is_alphanum_upper(s[l]))

            if self.is_alphanum_upper(s[l]) and self. is_alphanum_upper(s[r]):
                
                # print(l)
                # print(s[l], s[r])

                if s[l] != s[r]:
                    return False
                else:
                    l, r = l+1, r-1

            elif self.is_alphanum_upper(s[r]):
                l += 1     
            elif self.is_alphanum_upper(s[l]):
                r -= 1 
            else:
                l, r = l+1, r-1
            
        return True
            


    def is_alphanum_upper(self, c):

        check_num = ord('0') <= ord(c) and  ord(c) <= ord('9')
        check_alpha = ord('A') <= ord(c) and  ord(c) <= ord('Z') 

        return check_num or check_alpha



        
        