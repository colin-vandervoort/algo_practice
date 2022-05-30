class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """

        l, r = 0, 1
        max_p = 0

        while r < len(prices):
            if prices[l] < prices[r]:
                profit = prices[r] - prices[l]
                max_p = max(profit, max_p)
            else:
                l = r
            r += 1

        return max_p
