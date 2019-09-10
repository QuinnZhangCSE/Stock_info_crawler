import scrapy
import plotly.graph_objects as go
from datetime import datetime

class QuoteSpider(scrapy.Spider):
    name = "stock_price"
    
    def start_requests(self):
        #user input stock search
        self.target = input("\nPlease enter the stock symbol: ")
        url = "https://finance.yahoo.com/quote/" + self.target + "/history"
        yield scrapy.Request(url=url, callback=self.parse)
    
    def parse(self, response):
        chart = []
        for i in range(238):    #21 useless info before + 30 days * 7 info per day
            chart.append(response.xpath('//span/text()')[i].get())  #get the i-th text
        
        open_data = []
        high_data = []
        low_data = []
        close_data = []
        month_dict = {"Jan":1, "Feb":2, "Mar":3, "Apr":4, "May":5, "Jun":6, "Jul":7, "Aug":8, "Sep":9, "Oct":10, "Nov":11, "Dec":12}
        dates = []
        for i in range(28,238,7):
            #date example: "Sep 09, 2019"
            dates.append(datetime(year=int(chart[i][8:]), month=month_dict[chart[i][:3]], day=int(chart[i][4:6])))
            open_data.append(float(chart[i+1].replace(",","")))
            high_data.append(float(chart[i+2].replace(",","")))
            low_data.append(float(chart[i+3].replace(",","")))
            close_data.append(float(chart[i+4].replace(",","")))
        
        fig = go.Figure(data=[go.Candlestick(x=dates, open=open_data, high=high_data, low=low_data, close=close_data)])
        #add title, disable bottom rangeslider
        fig.update_layout(title=self.target + " Prices", xaxis_rangeslider_visible=False)
        fig.show()
