from argparse import ArgumentError
import datetime

# Construct a simple Portfolio class that has a collection of Stocks
# and a "Profit" method that receives 2 dates and returns the profit 
# of the Portfolio between those dates. Assume each Stock has a "Price"
# method that receives a date and returns its price. Bonus Track: make 
# the Profit method return the "annualized return" of the portfolio 
# between the given dates.


# To calculate the Annualize Return we need the Cumulative Return first
# And in order to calculate the Cumulative Return we need the initial price (PInitial) and the current price (PCurrent)
# Cumulative Return = (PCurrent/ PIntial) - 1
# Annualize Return = (1 + Cumulative Return)^(365/Days Held) - 1

# StockInstance is for saving the prices of the Stock in a certain point of time
class StockInstance:
    def __init__(self,price,date):
        self.price = price
        self.date = date


# The Stock class has a list of StockInstances
class Stock:
    def __init__(self, stockInstances):
        self.stockInstances = stockInstances
    
    # I assume that for each date there will be at most one stock with that exact date
    def price(self, date):
        result = [s for s in self.stockInstances if s.date == date]
        if(result == []):
            raise ValueError("There's no Stocks for the given date")
        return result[0].price

class Portfolio:
    def __init__(self, stock):
        self.stock = stock

    def __cumulativeReturn(self, pinitial, pcurrent):
        return (pcurrent/pinitial - 1)

    def profit(self, dateFrom, dateTo):
        cumulativeReturn = self.__cumulativeReturn(self.stock.price(dateFrom), self.stock.price(dateTo))
        daysHeld = (dateTo-dateFrom).days
        if(daysHeld<1):
            raise ValueError("dateFrom most be earlier than dateTo")
        return (1 + cumulativeReturn)**(365/daysHeld) - 1
        


# List of StockInstance for testing
testStockInstances = [
    StockInstance(
        100,
        datetime.datetime(2020,11,8)
    ),
    StockInstance(
        200,
        datetime.datetime(2022,11,8)
    )
]

stock = Stock(testStockInstances)

portfolio = Portfolio(stock)
print(portfolio.profit(datetime.datetime(2020,11,8), datetime.datetime(2022,11,8)))