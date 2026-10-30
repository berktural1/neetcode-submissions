class Solution:
    def maxProfit(self, prices: List[int]) -> int:

        # len is between 1 and 100, so I would assume O(nlogn) or
        # better
        
        # Value range doesn't change anything
        # just need to return max profit, don't have to keep track
        # of the indices

        max_prof = 0
        min_price = prices[0] # set minimum price to first value of
                              # range

        # naive approach: brute-force consider each
        # day as a buy opportunity and each following as a sell
        # O(n^2) time, O(1) extra space

        # better approach: two pointers
        # side note: best day to buy will always be the cheapest day
        # in the range

        i = 0   # buy
        j = i+1 # sell

        while j < len(prices):

            prof = prices[j] - prices[i]
            max_prof = max(max_prof, prof)

            if prices[j] < min_price:
                min_price = prices[j]
                i = j
                j += 1
            else:
                j += 1
        
        return max_prof

            
            





        