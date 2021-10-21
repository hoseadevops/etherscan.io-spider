import scrapy
# from scrapy import log
import logging

from spider.items import SmartContractItem

class SmartContractSpider(scrapy.Spider):

    name           = 'smart-contract'

    base_url       = "https://etherscan.io/"

    token_max_page = 3

    def start_requests(self):
        for p in range(1, self.token_max_page):
            url = self.base_url + 'tokens?p=' + str(p)
            yield scrapy.Request(url, self.parseToken)

    def parseToken(self, response):

        for each in response.xpath('//h3'):
            token_str     = each.xpath('./a/@href').extract_first()
            token         = token_str.split("/")[2]
            sub_url       = self.base_url + 'address/'+ token + '#code'

            yield scrapy.Request(sub_url, self.parseCode)

    def parseCode(self, response):
        item                  = SmartContractItem()

        name                  = response.xpath('//*[@id="ContentPlaceHolder1_tr_tokeninfo"]/td[2]/a/text()').extract_first()
        name                  = name.replace(' ','').replace(')','')
        item['token']         = response.xpath('//*[@id="mainaddress"]/text()').extract_first()
        item['contract']      = response.xpath('//*[@id="ContentPlaceHolder1_contractCodeDiv"]/div[2]/table/tr[1]/td[2]/text()').extract_first()
        item['contract']      = item['contract'].replace('\n', '')
        item['code']          = response.xpath('//*[@id="editor"]/text()').extract_first()
        item['name']          = name.split('(')[0] + '_' + name.split('(')[1] + '_' + item['token']


        logging.log(logging.DEBUG, 'token: ' + item['token'] + '\n' + 'name：' + item['name'])

        yield item
