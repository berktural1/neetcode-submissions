class Solution:
    def search(self, nums: List[int], target: int) -> int:
        
        # ascending -> binary search  
        # told O(logn) time but obvious given binary search is goal

        l = 0
        r = len(nums) - 1
        while l <= r: # want equality to check len of 1 example?

            mid = (l + r) // 2

            if nums[mid] < target:
                l = mid + 1
                continue
            elif nums[mid] > target:
                r = mid - 1
                continue
            else:
                return mid
        
        return -1

      


        