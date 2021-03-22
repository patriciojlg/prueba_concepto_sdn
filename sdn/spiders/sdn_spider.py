# -*- coding: utf-8 -*-
import scrapy


class SdnSpiderSpider(scrapy.Spider):
    name = 'sdn_spider'
    allowed_domains = ['sdn.cl']
    start_urls = ['https://www.sdn.cl/neumaticos.html']

    def parse(self, response):
        # cada uno de los productos
        sdn_product = response.xpath(
            '//*[@class="item product product-item"]')
        for i in sdn_product:
            price = i.xpath('.//*[@class="price"]/text()').get()
            link = i.xpath(
                './/div/div/h2/a/@href').get()
            yield scrapy.Request(url=link,
                                 callback=self.product_detail, meta={
                                     'price': price
                                 })

    def product_detail(self, response):
        price = response.meta["price"]
        stock = response.xpath('.//*[@class="stock available"]/span/text()').get()
        yield {
            "price": price,
            "stock": stock
        }
