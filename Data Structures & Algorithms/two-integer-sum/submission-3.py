class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:

        indices = {}

        # iterate through array to create dictionary of last seen
        # indices for each unique value ("key") in the array
        # allows for a list of indices to check against if duplicates
        for i,n in enumerate(nums):
            indices[n] = i
        
        # iterate over original array again
        # this time you check every element against the "last seen"
        # index dict to find matches that sum up to target.
        # able to differentiate between duplicates in the array
        # triplicates relevant to a solution are not possible due to the 
        # constraint that exactly one valid pair exists
        for i,n in enumerate(nums):
            complement = target - n

            # check if complement key exists in dict
            # also check to make sure you are not looking at the same  
            # index
            if complement in indices and i != indices[complement]:
                return [i,indices[complement]]
        
        return [] # base case, return the empty array

        






        