""" Say you have an array for which the ith element is the price of a given stock on day i."""
""" Design an algorithm to find the maximum profit. You may complete as many transactions as you like (ie, buy one and sell one share of the stock multiple times). However, you may not engage in multiple transactions at the same time (ie, you must sell the stock before you buy again)."""

def maxProfit(prices):
	max_profit = 0
	for i in xrange(1, len(prices)):
		gain = prices[i] - prices[i-1]
		if gain>0:
			max_profit += gain
	return max_profit


if __name__ == '__main__':
	prices = [1,2,1,2]
	print maxProfit(prices)
