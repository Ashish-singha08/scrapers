from scrapy.contrib.spiders import CrawlSpider, Rule
from scrapy.contrib.linkextractors.sgml import SgmlLinkExtractor
from scrapy.selector import HtmlXPathSelector
from scrapy.http import Request
from scrapy import log
from lookfantastic.items import lookfantasticItem

class lookfantasticSpider(CrawlSpider):
	name = "lookfantastic"
	allowed_domains = ["www.lookfantastic.com"]
	start_urls = [
		"http://www.lookfantastic.com/brands.dept",
		]

	rules = (
		Rule(SgmlLinkExtractor(allow=('brands/.*list'))), # product lists
		Rule(SgmlLinkExtractor(restrict_xpaths='//p[@class="product-name"]'), callback='parse_item') # item page
		)

	def parse_item(self, response):
		hxs = HtmlXPathSelector(response)
		item = lookfantasticItem()
		item["description"] = hxs.select('//div[@id="product-desc"]/div//p').extract()
		item["title"] = hxs.select('//div[@class="panel-head"]//h1/text()').extract()
		item["img_url"] = hxs.select('//div[@class="mImg"]/img/@src').extract()
		item["price"] = hxs.select('//span[@class="price-value"][@itemprop="price"]/text()').extract()[0].encode('ascii','ignore')
		item["volume"] = hxs.select('//span[@class="price-value"]/text()').extract()[1]
		return item
