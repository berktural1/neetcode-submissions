class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        # only one valid answer so can just return when you find it
        # len between 2 and 1000 -> O(n) ideal solution or better
        # values can be quite large but don't mean much

        # need to keep track of indices
        # need to make sure the indices i!=j 

        # smaller index first in return

        # naive: two pointer and iterate through all options
        # adding the values up until you find the right pair, return
        # O(n^2) time, O(1) space

        # another way to ask this is for a given number, is its   
        # complement in the array?

        # check for base case: if len==2 then it has to be the input
        # maybe not necessary but will catch this at the cost of one 
        # check. Won't write it in

        val_to_idx = {}

        for i in range(len(nums)):
            val_to_idx[nums[i]] = i # will overwrite with last seen if 
                                    # dups
        
        # now that we've created the dict with last seen index for each 
        # val:
        # iterate through again and see if each val's complement
        # is in the hashmap / dict

        for i in range(len(nums)):
            val = nums[i]
            complement = target - val

            if complement in val_to_idx:
                j = val_to_idx[complement]
                if i != j:
                    return [i,j]
            
        



                