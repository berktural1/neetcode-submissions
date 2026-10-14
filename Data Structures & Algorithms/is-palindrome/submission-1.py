class Solution:
    def isPalindrome(self, s: str) -> bool:
        
        s = s.upper()
        print(s)

        s_new = ''
        
        for i in range(len(s)): # O(n)
            # 7N ops total, if adding to existing string is O(1) which I am not sure it is
            if ( 48 <= ord(s[i]) <= 57 ) or (65 <= ord(s[i]) <= 90):
                s_new += s[i]
        
        if len(s_new) == 1:
            return True
        
        for i in range(len(s_new)):
            j = -(i+1)
            print(s_new[i], s_new[j])
            if ord(s_new[i]) != ord(s_new[j]):
                return False
        
        return True