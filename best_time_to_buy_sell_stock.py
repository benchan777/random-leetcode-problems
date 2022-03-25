def maxProfit(prices):
  max_profit = 0
  left = 0
  right = 0
  minimum = prices[left]
  
  for i in range(len(prices)):
    if prices[i] < minimum:
      minimum = prices[i]
      left = i
    if prices[right] - prices[left] > 0:
      max_profit = max(max_profit, prices[right] - prices[left])
      right += 1
    else:
      right += 1
      
  return max_profit

def maxProfit2(prices):
  max_profit = 0
  minimum = prices[0]

  for price in prices:
    if price < minimum:
      minimum = price
    max_profit = max(max_profit, price - minimum)
  return max_profit

print(maxProfit2([7,1,5,3,6,4]))