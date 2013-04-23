from scrapy.contrib.spiders import CrawlSpider, Rule
from scrapy.contrib.linkextractors.sgml import SgmlLinkExtractor
from scrapy.selector import HtmlXPathSelector
from scrapy.http import Request
from scrapy import log
from dealextream.items import DealextreamItem
 
class iherbSpider(CrawlSpider):
	name = "dealextream"
	allowed_domains = ["dx.com"]
	start_urls = [
        "http://dx.com/SiteMap",
    	]
	rules = (
	        Rule(SgmlLinkExtractor(allow='c/.*')), # list page
        	Rule(SgmlLinkExtractor(allow='p/.*'), callback="parse_item") # item page
		)
 	
	def parse_item(self, response):
	    	hxs = HtmlXPathSelector(response)
	        item = DealextreamItem()
        	item["description"] = hxs.select('//div[@id="overview"]/div//div').extract()
		item["title"] = str(hxs.select('//div[@class="pinfo_wrapper"]/h1/text()').extract()).replace("    ","").replace("\\r\\n","")
	        item["img_url"] = hxs.select('//div[@id="midPicBox"]/a/img/@src').extract()
	        item["price"] = hxs.select('//span[@id="price"]/text()').extract()
	        return item
