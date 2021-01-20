prices = [7,6,4,3,1]
profit = 0
size = len(prices)
for i in range(size - 1):
    if prices[i] < prices[i+1]:
        profit += prices[i+1] - prices[i]
print(profit)