import numpy as np


#list comp to read in the stock prices for tesla (converts to float and rounds)
prices = [round(float(line), 2) for line in reversed(open("/home/ubuntu/data3500_homework/HW4/TSLA.txt").readlines())]

i = 0 #indexing value to keep track
buy = 0
total_profit = 0
first_buy = 0 # index for first buy
# need to loop through prices list
for price in prices:
    if i >= 5:
        current_price = price
        # 5 day moving average
        average = (prices [i-1] + prices[i-2] + prices [i-3] + prices [i-4] + prices [i-5])/5 #average price for the 5 previous

        if current_price < average * 0.98 and buy == 0: #
            buy = current_price # buy stock if meets criteria
            print ("Buying At: ", round (current_price, 2))
            # store first buy price
            if first_buy == 0: # note this will only trigger the first time a stock is bought and then not again 
                first_buy += current_price
        elif current_price > average * 1.02 and buy != 0:
            print("Selling At: ", round (current_price,2)) # sell stock if meets criteria
            # calculate trade profit (how much money made)
            trade_profit = current_price - buy
            total_profit += trade_profit
            print("Trade Profit: ", round (trade_profit,2))
            buy = 0 # reset buy variable after selling
        else:
            pass
    # move to next day in list
    i += 1
print ("Total Profit: ", round (total_profit,2))
# if there was a first buy, calculate final profit percentage
# print the first buy and & return rounded to 2 decimals
if first_buy != 0:
    final_profit_percentage = (total_profit / first_buy) * 100
    print("First Buy: ", round(first_buy, 2))
    print("% return:", round(final_profit_percentage, 2))




#### Past efforts for documentation :)
"""
# for i in range(len(prices)):
#     if i <= len(prices)-5:
#         if len(prices) >= 5:
#             average = sum(prices[0+i:5+i])/5
# """

# #est the needed var
# buy = 0 
# total_profit = 0 
# first_buy = 0
# first_price = prices[0]
# num_prices = len(prices) 

# #finding the average 
# for i in range(len(prices)):
#     if i <= len(prices)-5:
#         if len(prices) >= 5:
#             average = sum(prices[0+i:5+i])/5 #have the index values move through the list
#         if price < average * 0.98: #it dips below so buy
#             if buy == 0:
#                 first_buy += price 
#             buy += price
#             print("buying at:", price)
                
        
#         elif price > average * 1.02 and buy != 0: #it dips above so sell for prifit 
#             selling = price
#             print("Selling at: ", selling)
#             trading_profit = selling - buy # calc the profit 
#             print("Trading Profit: ", trading_profit)
#             total_profit += trading_profit
#             buy = 0
#         else: 
#             pass

# print("Total Profit: ", total_profit)
# print("First Buy: ", first_buy)
# final_profit_percentage = ( total_profit / first_buy ) * 100
# print(F"% return: {final_profit_percentage}") ## F








# """"
# The official way
# """
# i = 0
# for price in prices: 
#     current_price = price
#     if i > :
#         average = (prices[i-1] + prices[i-2] + prices[i-4] +prices[i-5])/5
#     i += 1


