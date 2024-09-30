def maxProfit(self, prices: List[int]) -> int:
    buyPrice = 0
    maxProfit = 0
    for sellPrice in range(1,len(prices)):
        if prices[sellPrice] < prices[buyPrice]:
        buyPrice = sellPrice
        else:
            currentProfit = prices[sellPrice] - prices[buyPrice]
            if currentProfit > maxProfit:
                maxProfit = currentProfit
return maxProfit