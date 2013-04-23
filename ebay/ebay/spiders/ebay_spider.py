from scrapy.contrib.spiders import CrawlSpider, Rule
from scrapy.contrib.linkextractors.sgml import SgmlLinkExtractor
from scrapy.selector import HtmlXPathSelector
from scrapy.http import Request
from scrapy import log
from ebay.items import ebayItem
 
class ebaybSpider(CrawlSpider):
	name = "ebay"
	allowed_domains = ['ebay.com']
	start_urls = [
		"http://listings.ebay.com/_W0QQfclZ1QQsocmdZListingCategoryList",
		]
	rules = (
		Rule(SgmlLinkExtractor(allow='.*shop.ebay.com.*')), # list page
		Rule(SgmlLinkExtractor(allow='sch/.*')), # list page
		Rule(SgmlLinkExtractor(allow='itm/.*'), callback="parse_item") # item page
		)
	def parse_item(self, response):
		hxs = HtmlXPathSelector(response)
		item = ebayItem()
		print(hxs.select('//div[@class="u-flL"]').extract())
		print(hxs.select('//li[@class]/input'))
		print(response)
		print("aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa")
		if (hxs.select('//div[@id="u-flL"]/a["@id"]').extract()!="binBtn_btn"): 	
			pass
		else:
			item["description"] = str(hxs.select('//div[@class="tb-cw"]//text()').extract()).replace("\r\n","").encode('ascii','ignore')
			item["title"] = hxs.select('//h1[@class="vi-is1-titleH1"]/text()').extract()[0].strip()
			item["img_url"] = hxs.select('img[@id="icImg"][@src]').extract()
			item["price"] = hxs.select('//span[@class="vi-is1-prcp"]/text()').extract()[0].encode('ascii','ignore')
			item["shipment"] = hxs.select('//span[@id="fshippingCost"]/text()').extract()
			return item
