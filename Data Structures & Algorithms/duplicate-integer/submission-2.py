class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:

        n_dict = {}

        # base case check first
        if len(nums) == 0:
            return False

        for i,n in enumerate(nums): #index, key
            if n in n_dict: # O(1) retrieval
                return True
            else:
                n_dict[n] = i # O(1) setting
        return False





        





        