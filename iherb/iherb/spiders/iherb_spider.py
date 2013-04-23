from scrapy.contrib.spiders import CrawlSpider, Rule
from scrapy.contrib.linkextractors.sgml import SgmlLinkExtractor
from scrapy.selector import HtmlXPathSelector
from scrapy.http import Request
from scrapy import log
from iherb.items import IherbItem
 
class iherbSpider(CrawlSpider):
    name = "iherb"
    allowed_domains = ["www.iherb.com"]
    start_urls = [
        "http://www.iherb.com/BrandsAZ?cid=1",
    ]
 
    rules = (
        Rule(SgmlLinkExtractor(restrict_xpaths='//ul[@class="ac"]/li/a[@href]')), # list page
        Rule(SgmlLinkExtractor(restrict_xpaths='//div[@class="ProductItem_Name"]/a[@href]'), callback="parse_item") # item page
        )
 
    def parse_item(self, response):
        hxs = HtmlXPathSelector(response)
        item = IherbItem()
        strings = hxs.select('//td[@id="div_Content"]').extract()
	c=0#initializing counter
	for a in strings: #erasing not neaded charecters
		a=a.replace("\r\n","").replace("   ","").encode('ascii','ignore')
		strings[c]=a#replacing the sting in the list
		c=c+1
	item["description"]=strings
        item["title"] = hxs.select('//h1[@class="Title_Blu B"]/text()').extract()[0].strip()
        item["img_url"] = hxs.select('//a[@id="yamaha"]/img/@src').extract()
        item["price"] = hxs.select('//span[@id="ctl00_StorePageContents_ProductDetailsCtl_lblPrice"]/text()').extract()[0].encode('ascii','ignore')
        return item
