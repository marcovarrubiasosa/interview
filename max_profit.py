def maxProfit(prices: List[int]) -> int:
    min_price = float('inf')
    max_profit = 0

    for price in prices:
        if price < min_price:
            min_price = price
        else:
            max_profit = max(max_profit, price - min_price)
    return max_profit

assert maxProfit([7,6,4,3,1]) == 0
assert maxProfit([7,1,5,3,6,4]) == 5
assert maxProfit([]) == 0
