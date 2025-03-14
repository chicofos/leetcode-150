# You are given an array prices where prices[i] is the price of a given stock on the ith day.
# You want to maximize your profit by choosing a single day to buy one stock and choosing a different day in the future to sell that stock.
# Return the maximum profit you can achieve from this transaction. If you cannot achieve any profit, return 0.

def maxProfit(prices):
        price_min = prices[0]
        price_max = 0 
        profit = 0
        
        for price in prices:
            if price < price_min:
                price_min = price
                price_max = price
            elif price > price_max:
                price_max = price
                profit = max(price_max - price_min, profit) 
        return profit
    
    #Time complexity O(n)
    #Space Complexity O(1)
    
print(maxProfit([7,1,5,3,6,4]))