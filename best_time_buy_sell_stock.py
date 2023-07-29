# given the prices of stock maximize your profit by choosing a single day to buy one stock and
# choosing a different day in the future to sell that stock and return profit
def buysell(prices):
    buy = prices[0]
    profit = 0

    for sell in prices[1:]:
        if sell > buy:
            profit = max(profit, sell-buy)
        elif sell <= buy:
            buy = sell

    return profit

print(buysell([7,1,5,3,6,4,1,13]))