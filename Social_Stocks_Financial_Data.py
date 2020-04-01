#Code to pull data from Yahoo! Finance and store it as a CSV file to use in R.

#import necessary packages, installation instructions are online
import yfinance as yf
import pandas

#Define stock you want
stock = yf.Ticker("TSLA")

#create a file for the most recent overview of your stock, choose a location to save file
#should create a file for every stock we look at, need to remember to change the name of the file
stock_file = open(r"C:/Users/acanfj/Dropbox/spring_2020/Systems Engineering and Social Media/Project/tsla_overview.txt", "a")

#pull data on stock, initially stored as a dictionary
stock_dict = stock.info

#iterate through and store all data as a line in the file
for key in stock_dict:
    in_str = str(key) + " : " + str(stock_dict[key]) + "\n"
    stock_file.write(in_str)
stock_file.close()

#get history of stock performance over desired period, save as a CSV file to use in R
stock_hist = stock.history(period = "6mo")
stock_hist.to_csv('C:/Users/acanfj/Dropbox/spring_2020/Systems Engineering and Social Media/Project/tsla_data.csv', index = True)
