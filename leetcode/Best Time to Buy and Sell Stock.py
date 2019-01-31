class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        #if prices.sort(reverse=True) == prices:
        #    return 0
        profit = 0
        for i in range(len(prices)-1):
            a = prices[i+1] - prices[i]
            if a > 0:
                profit = a + profit
        return profit
