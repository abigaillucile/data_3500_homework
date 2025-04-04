import json


#comment out print statements in the functions
def meanReversionStrat(prices, name):
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
                # print ("Buying At: ", round(current_price, 2))
                # store first buy price
                if first_buy == 0: # note this will only trigger the first time a stock is bought and then not again 
                    first_buy += current_price
            elif current_price > average * 1.02 and buy != 0:
                # print("Selling At: ", round(current_price,2)) # sell stock if meets criteria
                # calculate trade profit (how much money made)
                trade_profit = current_price - buy
                total_profit += trade_profit
                # print("Trade Profit: ", round(trade_profit, 2))
                buy = 0 # reset buy variable after selling
            else:
                pass
        # move to next day in list
        i += 1
    # print ("Total Profit: ", round(total_profit, 2))
    # if there was a first buy, calculate final profit percentage
    # print the first buy and & return rounded to 2 decimals
    if first_buy != 0:
        final_profit_percentage = (total_profit / first_buy) * 100
        # print("First Buy: ", round(first_buy, 2))
        # print("Percent return:", round(final_profit_percentage, 2))
        # percent return = (currentt price - buy)/buy price
    else:
        pass
    # i += 1
    #get the return
    return total_profit, final_profit_percentage  #input percent return variable here 

def simpleMovingAvg(prices, name):
    i = 0  # indexing value to keep track
    buy = 0
    total_profit_SMA = 0  # Fixed variable name
    first_buy = 0  # index for first buy
    
    for price in prices:
        if i >= 5:
            current_price = price
            # 5 day moving average
            average = (prices[i-1] + prices[i-2] + prices[i-3] + prices[i-4] + prices[i-5])/5  # average price
            
            if price > average and buy == 0:
                buy = current_price
                if first_buy == 0:  # Track the first buy price for percentage calculation
                    first_buy = current_price
                print(f"buy at: {price}")
                
            elif price < average and buy != 0:
                trade_profit = current_price - buy
                total_profit_SMA += trade_profit
                buy = 0
                print(f"sell at: {price}")
            else:
                pass
        
        i += 1
    
    # Calculate final profit percentage
    if first_buy != 0:
        final_profit_percentage_SMA = (total_profit_SMA / first_buy) * 100
    else:
        final_profit_percentage_SMA = 0  # Handle case where no trades were made
        
    return total_profit_SMA, final_profit_percentage_SMA

def saveResults(dictionary):
    with open("/home/ubuntu/data3500_homework/HW5/results.json", "w") as file:
        json.dump(dictionary, file, indent=4)


results = {}


tickers = ["ADBE", "AMZN", "AAPL", "COKE", "GIS", "IP", "KDP", "NKE", "TQQQ", "TSLA"]
#read in ten files for a loop 


for ticker in tickers: 
    #isolate the prices for each ticker
    prices = [round(float(line), 2) for line in reversed(open("/home/ubuntu/data3500_homework/HW5/"+ticker+".txt").readlines())]
    
    #run the mean reversion strat and store the two return outputs to the thwo var mr_profit and mr_return
    MR_profit, MR_return = meanReversionStrat(prices, ticker) #this will run the logic on all the prices for each stock specified in ticker 
    SMA_profit, SMA_return = simpleMovingAvg(prices, ticker)

# get the profit and return % form the functions and save the to the ditionary 
    results[ticker+"_prices"] = prices
    results[ticker+"_MR_profit"] = MR_profit
    results[ticker+"_MR_returns"] = MR_return
    results[ticker+"_SMA_profit"] = SMA_profit
    results[ticker+"_SMA_returns"] = SMA_return

saveResults(results)