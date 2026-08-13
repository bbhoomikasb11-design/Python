prices = [7,10, 1, 3, 6]
def maxProfit(prices):
    min_profit = float('inf')
    max_profit = 0
    for price in prices:
        if price < min_profit:
            min_price = price
        profit = price - min_profit
        if profit > max_profit:
            max_profit = profit
    return max_profit
print(maxProfit(prices))