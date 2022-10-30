import scrapy
from scrapypractise.items import ScrapypractiseItem


class TilesSpider(scrapy.Spider):
    name = 'tiles'
    allowed_domains = ['magnatiles.com']
    start_urls = ['https://www.magnatiles.com/products/']

    def parse(self, response):
        item = ScrapypractiseItem()
        rel_img_urls = response.css('img::attr(src)').extract()
        item['image_urls'] = self.url_join(rel_img_urls, response)
        return item

    def url_join(self, rel_img_urls, response):
        joined_urls = []
        for rel_img_url in rel_img_urls:
            joined_urls.append(response.urljoin(rel_img_url))

        return joined_urls
