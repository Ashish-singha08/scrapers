# Scrapy settings for lookfantastic project
#
# For simplicity, this file contains only the most important settings by
# default. All the other settings are documented here:
#
#     http://doc.scrapy.org/topics/settings.html
#

BOT_NAME = 'lookfantastic'
BOT_VERSION = '1.0'

SPIDER_MODULES = ['lookfantastic.spiders']
NEWSPIDER_MODULE = 'lookfantastic.spiders'
USER_AGENT = '%s/%s' % (BOT_NAME, BOT_VERSION)

# LOG_FILE = 'crawl.log'