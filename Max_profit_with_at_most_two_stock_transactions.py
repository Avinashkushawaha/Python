def max_profit(prices):
    t1_cost = t2_cost = float('inf')
    t1_profit = t2_profit = 0
    for p in prices:
        t1_cost = min(t1_cost, p)
        t1_profit = max(t1_profit, p - t1_cost)
        t2_cost = min(t2_cost, p - t1_profit)
        t2_profit = max(t2_profit, p - t2_cost)
    return t2_profit

print(max_profit([3,3,5,0,0,3,1,4]))  # 6
