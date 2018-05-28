import scrapy

from spider.items import SmartContractItem

class SmartContractSpider(scrapy.Spider):

    name           = 'smart-contract'

    base_url       = "https://etherscan.io/"

    token_max_page = 2

    def start_requests(self):
        for p in range(1, self.token_max_page):
            url = self.base_url + 'tokens?p=' + str(p)
            yield scrapy.Request(url, self.parseToken)

    def parseToken(self, response):

        for each in response.xpath('//h5'):
            token_str     = each.xpath('./a/@href').extract_first()
            token         = token_str.split("/")[2]
            sub_url       = self.base_url + '/address/'+ token + '#code'

            yield scrapy.Request(sub_url, self.parseCode) 

            print(token)
        

    def parseCode(self, response):
        item                  = SmartContractItem()

        item['name']          = response.xpath('//*[@id="ContentPlaceHolder1_divSummary"]/div[1]/table/thead/tr/th/font/text()').extract_first()
        item['token']         = response.xpath('//*[@id="mainaddress"]/text()').extract_first() 
        item['code']          = response.xpath('//*[@id="editor"]/text()').extract_first()
        
        print(item)

        yield item

        return item
        

        

