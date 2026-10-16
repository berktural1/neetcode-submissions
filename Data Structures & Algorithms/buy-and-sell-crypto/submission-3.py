class Solution:
    def maxProfit(self, prices: List[int]) -> int:

        # key idea here: you can learn information from the sub-problem
        # -> DP

        # first thought, naive solution: O(n2) time, O(1) extra space
        # 2nd: can solve w/ 2 pointers

        # going w/ DP approach

        # key idea here I have missed before: lowest price will always be the best buy

        i = 0
        j = 1

        # base case
        maxProf = 0
        minPrice = prices[i]

        while j < len(prices):

            # do i index and check for j or i?

            maxProf = max(prices[j] - prices[i], maxProf)

            if prices[j] < minPrice:
                minPrice = prices[j]
                i = j # is this a pointer? will it overwrite?
            
            j += 1
        
        return maxProf
            

            


        