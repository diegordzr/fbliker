# -*- coding: utf-8 -*-

# Scrapy settings for fbliker project
#
# For simplicity, this file contains only the most important settings by
# default. All the other settings are documented here:
#
#     http://doc.scrapy.org/en/latest/topics/settings.html
#

BOT_NAME = 'fbliker'

SPIDER_MODULES = ['fbliker.spiders']
NEWSPIDER_MODULE = 'fbliker.spiders'

# Crawl responsibly by identifying yourself (and your website) on the user-agent
USER_AGENT = "Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:34.0) Gecko/20100101 Firefox/34.0"
