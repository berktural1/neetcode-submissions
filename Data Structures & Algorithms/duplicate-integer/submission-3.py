class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:

        # base case check: empty -> false
        # immediate thought because of dups is hashmap
        # naive appraoch would be brute force at O(N^2) time O(1) space
        # hashmap is O(N) time but O(N) space. So there is a tradeoff
        if nums:
            seen = {}

            for n in nums:
                if n in seen:
                    return True
                else:
                    seen[n] = 1
            # return False if you ahve gone through the entire list
            # and no dups
            return False

        else:
            return False

        # tests: 
        # empty list edge case
        