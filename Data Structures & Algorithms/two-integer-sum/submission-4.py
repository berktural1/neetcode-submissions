class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:

        # make dictionary of values, only keeping last seen index
        seen = {}
        for i in range(len(nums)):
            seen[nums[i]] = i
        
        # another way to ask this is if the complement exists in the list
        for i,k in enumerate(seen):
            compl = target - k
            if compl in seen and seen[compl] != i:
                return [i,seen[compl]] # compl is guaranteed to be greater?
        
        return []
        