# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/topics/items.html

from scrapy.item import Item, Field

class IherbItem(Item):
    # define the fields for your item here like:
	title = Field()
	price = Field()
	img_url = Field()
	description = Field()
