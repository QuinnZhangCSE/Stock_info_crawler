import scrapy

class QuoteSpider(scrapy.Spider):
    name = "quotes"
    
    def start_requests(self):
        target = "GOOG"
        url = "https://finance.yahoo.com/quote/" + target + "/history"
        yield scrapy.Request(url=url, callback=self.parse)
    
    def parse(self, response):
        chart = []
        for info in response.xpath('//span/text()').getall():
            chart.append(info)
        #chart = chart[28:238]
        day_info = []
        for i in range(21,238,7):
            day_info.append(chart[i:i+7])
        for info in day_info:
            print(info)
