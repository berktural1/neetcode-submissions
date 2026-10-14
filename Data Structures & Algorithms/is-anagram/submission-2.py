class Solution:
    def isAnagram(self, s: str, t: str) -> bool:

        # length check first
        if len(s) != len(t):
            return False

        # create empty dictionarys
        s_freq = {}
        t_freq = {}
        
        # now we know the lens have to be equal
        # is there a better way to do this?
        for i in range(len(s)):
            if s[i] not in s_freq:
                s_freq[s[i]] = 1
            else:
                s_freq[s[i]] += 1

            if t[i] not in t_freq:
                t_freq[t[i]] = 1
            else:
                t_freq[t[i]] += 1
        
        # simply return the result of the equality check on dicts
        return s_freq == t_freq
            


        
        