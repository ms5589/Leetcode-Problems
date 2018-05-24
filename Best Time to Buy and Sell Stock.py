'''
Say you have an array for which the ith element is the price of a given stock on day i.

If you were only permitted to complete at most one transaction (i.e., buy one and sell one share of the stock), design an algorithm to find the maximum profit.

Note that you cannot sell a stock before you buy one.
'''
class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        if(len(prices)==0):
            return 0
        buy = prices[0]
        profit = 0
        store = []
        for i in range(1,len(prices)):
            if(prices[i] > buy):
                sell = prices[i]
                profit = sell - buy
                store.append(profit)
            if(prices[i] < buy):
                buy = prices[i]
                print buy
            
        if(len(store)>1):
            return max(store)
        else:
            return profit
