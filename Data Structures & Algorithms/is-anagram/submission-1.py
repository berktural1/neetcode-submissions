class Solution:
    def isAnagram(self, s: str, t: str) -> bool:

        s_dict = {}
        t_dict = {}

        if len(s) == len(t):

            for c in s:
                if c in s_dict:
                    s_dict[c] += 1
                else:
                    s_dict[c] = 1
            
            for c in t:
                if c in t_dict:
                    t_dict[c] += 1
                else:
                    t_dict[c] = 1
            return t_dict == s_dict
        else:
            return False

        return 


        