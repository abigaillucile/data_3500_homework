import json
import requests


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
                if i < len(prices-1):
                    print(f"You should buy {ticker} today! (According to Mean Reversion Strategy)")
                if first_buy == 0: # note this will only trigger the first time a stock is bought and then not again 
                    first_buy += current_price
            elif current_price > average * 1.02 and buy != 0:
                if i < len(prices-1):
                    print(f"You should sell {ticker} today! (According to Mean Reversion Strategy)")
                trade_profit = current_price - buy
                total_profit += round(trade_profit,2)
                buy = 0 # reset buy variable after selling
            else:
                pass
        # move to next day in list
        i += 1
    # if there was a first buy, calculate final profit percentage
    # print the first buy and & return rounded to 2 decimals
    if first_buy != 0:
        final_profit_percentage = round(((total_profit / first_buy) * 100),2) 
        # percent return = (currentt price - buy)/buy price
    else:
        pass
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
                if i < len(prices-1):
                    print(f"You should buy {ticker} today! (According to Simple Moving Average Strategy)")
                if first_buy == 0:  # Track the first buy price for percentage calculation
                    first_buy = current_price
                
            elif price < average and buy != 0:
                if i < len(prices-1):
                    print(f"You should sell {ticker} today! (According to Simple Moving Average Strategy)")
                trade_profit = current_price - buy
                total_profit_SMA += round(trade_profit,2)
                buy = 0
            else:
                pass
        
        i += 1
    
    # Calculate final profit percentage
    if first_buy != 0:
        final_profit_percentage_SMA = round(((total_profit_SMA / first_buy) * 100),2) 
    else:
        pass
        
    return total_profit_SMA, final_profit_percentage_SMA

def bollingerBands(prices, name):
    i = 0  # indexing value to keep track
    buy = 0
    total_profit_SMA = 0  # Fixed variable name
    first_buy = 0  # index for first buy
    
    for price in prices:
        if i >= 5:
            current_price = price
            # 5 day moving average
            average = (prices[i-1] + prices[i-2] + prices[i-3] + prices[i-4] + prices[i-5])/5  # average price
            
            if price > average*1.05 and buy == 0:
                buy = current_price
                if i < len(prices-1):
                    print(f"You should buy {ticker} today! (According to Bollinger Bands)")
                if first_buy == 0:  # Track the first buy price for percentage calculation
                    first_buy = current_price
                
            elif price < average*0.95 and buy != 0:
                if i < len(prices-1):
                    print(f"You should sell {ticker} today! (Bollinger Bands Strategy)")
                trade_profit = current_price - buy
                total_profit_BB += round(trade_profit,2)
                buy = 0
            else:
                pass
        
        i += 1
    
    # Calculate final profit percentage
    if first_buy != 0:
        final_profit_percentage_SMA = round(((total_profit_SMA / first_buy) * 100),2) 
    else:
        pass
        
    return total_profit_BB, final_profit_percentage_BB

def saveResults(dictionary):
    with open("/home/ubuntu/data3500_homework/final/results.json", "w") as file:
        json.dump(dictionary, file, indent=4)

#def a fucntion to pull the inital data from api's (this is in the code from last thurs)
def initialDataPull(tickers):
    for ticker in tickers:
        url = "http://www.alphavantage.co/query?function=TIME_SERIES_DAILY&symbol="+ticker+"&outputsize=full&apikey=NG9C9EPVYE" #this may not work...
        # making the API call for our stock
        request = requests.get(url)
        request_dictionary = json.loads(request.text)
        # keys
        key_1 = "Time Series (Daily)"
        key_2 = "4. close" #references the close prices in the api 
        lines = []
        for date in request_dictionary[key_1].keys():
            lines.append(date + "," + request_dictionary[key_1][date][key_2] + "\n")
        lines = lines[::-1]
        with open("/home/ubuntu/data3500_homework/final/"+ticker+".csv","w") as file:
            file.writelines(lines)

def appendData(tickers):
    #track the last date added to the file 
    for ticker in tickers:
        url = "http://www.alphavantage.co/query?function=TIME_SERIES_DAILY&symbol="+ticker+"&outputsize=full&apikey=NG9C9EPVYE"
        # making the API call for our stock
        request = requests.get(url)
        request_dictionary = json.loads(request.text)
        # keys
        key_1 = "Time Series (Daily)"
        key_2 = "4. close"

        with open("/home/ubuntu/data3500_homework/final/"+ticker+".csv", "r") as file: 
            csv_lines = file.readlines()

        #getting the most recent date from csv file 
        latest_date = csv_lines[-1].split(",")[0] #gives just the date/string to compare in the api and append 
        print(latest_date)
        new_lines = []
        for date in request_dictionary[key_1].keys():
            if date == latest_date: #if the last date is the same don't pull!!
                break #when this breaks it won't keep checking earlier dates so you're good!!
            else: 
                new_lines.append(date + "," + request_dictionary[key_1][date][key_2] + "\n")
        
        new_lines = new_lines[::-1] #reverse the lines 
        #add new data!!!
        with open("/home/ubuntu/data3500_homework/final/"+ticker+".csv", "a") as file: 
            file.writelines(new_lines)
    

results = {}
most_profit = 0 
best_strat = ""
best_ticker = ""

tickers = ["ADBE", "AMZN", "AAPL", "COKE", "GIS", "IP", "KDP", "NKE", "TQQQ", "TSLA"] #just for testing purposes
#read in ten files for a loop 

# initialDataPull(tickers) #once all data is in, comment this line out

appendData(tickers)

for ticker in tickers: #this probably needs to change....?
    #isolate the prices for each ticker
    prices = [round(float(line), 2) for line in reversed(open("/home/ubuntu/data3500_homework/final/"+ticker+".txt").readlines())]
    
    #run the mean reversion strat and store the two return outputs to the thwo var mr_profit and mr_return
    MR_profit, MR_return = meanReversionStrat(prices, ticker) #this will run the logic on all the prices for each stock specified in ticker 
    SMA_profit, SMA_return = simpleMovingAvg(prices, ticker)
    BB_profit, BB_return = bollingerBands(prices, ticker)

    # get the profit and return % form the functions and save the to the ditionary 
    results[ticker+"_prices"] = prices
    results[ticker+"_MR_profit"] = MR_profit
    results[ticker+"_MR_returns"] = MR_return
    results[ticker+"_SMA_profit"] = SMA_profit
    results[ticker+"_SMA_returns"] = SMA_return
    results[ticker+"_BB_profit"] = BB_profit
    results[ticker+"_BB_returns"] = BB_return


    #this checks to see what ticker and strat was the most profitable 
    if MR_profit > most_profit: 
        most_profit = MR_profit
        best_strat = "Mean Reversion"
        best_ticker = ticker 
    elif SMA_profit > most_profit: 
        most_profit = SMA_profit
        best_strat = "Simple Moving Average"
        best_ticker = ticker 
    elif BB_profit > most_profit: 
        most_profit = BB_profit
        best_strat = "Bollinger Bands"
        best_ticker = ticker 

print(f"The stock that made the most profit was {best_ticker} with a profit of {most_profit} using the {best_strat}.")

saveResults(results)



