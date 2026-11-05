class Solution:
    def search(self, nums: List[int], target: int) -> int:

        # sorted list -> binary search
        # told the solution must be O(logn) time but that
        # is obvious because binary search is the solution

        # O(logn) time, O(1) extra space
        # other solutions:
        # brute force O(n) time, O(1) extra space
        

        # set initial pointers
        low = 0
        high = len(nums) - 1 

        while low <= high:

            mid = (low + high) // 2

            if nums[mid] > target:
                high = mid - 1 # don't need to consider element
                               # you have already checked
            elif nums[mid] < target:
                low = mid + 1
            else:
                return mid
        
        return -1
        