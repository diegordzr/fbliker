import re
from urlparse import urljoin

from scrapy import Item, Field
from scrapy.http import Request

from facebook_login import FacebookLogin
import time

class FbFeed(Item):
    who = Field()
    message = Field()
    uri_like = Field()


class FacebookStories(FacebookLogin):
    name = "fb_stories"
    start_urls = ["https://m.facebook.com/stories.php"]

    def after_login(self, response):
        for url in self.start_urls:
            yield Request(url, callback=self.parse_stories)

    def parse_stories(self, response):
        self.log('search stories')
        stories = response.xpath('//div[@id="m-top-of-feed"]/following-sibling::div[1]/div')

        while True:
            for story in stories:
                yield self.check_like(story)
            break
            time.sleep(60)

    def check_like(self, response):
        uri_profiles = response.css('strong a::attr(href)').extract()
        profiles_id = []
        for up in uri_profiles:
            profiles_id.append(self.find_between(up, '/', '?fref'))

        for user in profiles_id:
            self.log("check like for: " + user)
            if user != '' and user in open('fbliker/data/fb_users.txt').read():
                self.log("like request for " + user)
                query_string = "".join(response.xpath('.//a[contains(@href, "/a/like.php")]/@href').extract())
                return Request('https://m.facebook.com' + query_string, callback=self.response_like)
        return None

    def response_like(self, response):
        response = response.xpath('//div[@id="m-top-of-feed"]/following-sibling::div[1]/div')[0]
        query_string = "".join(response.xpath('.//a[contains(@href, "/a/like.php")]/@href').extract())
        uri = 'https://m.facebook.com' + query_string
        uri_profiles = response.css('strong a::attr(href)').extract()
        profiles_id = []
        for up in uri_profiles:
            profiles_id.append(self.find_between(up, '/', '?fref'))

        story = FbFeed()
        story['who'] = {
            'name': response.css('strong *::text').extract(),
            'id': profiles_id
        }
        story['message'] = "".join(response.xpath('div[1]/div/following-sibling::div').css('*::text').extract())
        story['uri_like'] = uri
        return story

    def find_between(self, s, first, last):
        try:
            start = s.rindex(first) + len(first)
            end = s.rindex(last, start)
            return s[start:end]
        except ValueError:
            return ""
