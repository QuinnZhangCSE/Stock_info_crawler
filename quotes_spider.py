import scrapy

class QuoteSpider(scrapy.Spider):
    name = "stock_price"
    
    def start_requests(self):
        target = "GOOG"
        #enable custom stock search
        url = "https://finance.yahoo.com/quote/" + target + "/history"
        yield scrapy.Request(url=url, callback=self.parse)
    
    def parse(self, response):
        chart = []
        for i in range(238):    #21 useless info before + 30 days * 7 info per day
            chart.append(response.xpath('//span/text()')[i].get())  #get the i-th text
            
        #what the numbers mean everyday
        info_type = chart[21:28]
        
        day_info = []
        for i in range(28,238,7):
            day = []
            for j in range(0,7):
                day.append(info_type[j] + ": " + chart[i+j])    #add info type in front of context
            day_info.append(day)
        
        #print the information
        for info in day_info:
            print(info)
