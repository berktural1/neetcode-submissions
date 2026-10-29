class Solution:
    def isAnagram(self, s: str, t: str) -> bool:

        # brute force: O(n^2) time O(n) extra space
        # sorting then checking equality:
            # O(nlogn) time, O(1) extra space, if sorting in place
        # hash map is better, take advantage of O(1) query and      
        # assignment
            # O(n) time O(n) extra space

        # note: only contain lower case letters so don't need to 
        # consider that wrinkle
        
        freq_s = {}
        freq_t = {}

        if len(s) == len(t): # base case check
            for i in range(len(s)):
                if s[i] not in freq_s:
                    freq_s[s[i]] = 1
                if t[i] not in freq_t:
                    freq_t[t[i]] = 1
                
                freq_s[s[i]] += 1
                freq_t[t[i]] += 1
            
            return freq_s == freq_t

        else:
            return False


        