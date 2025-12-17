import scrapy
from quotesbot.items import QuotesbotItem


class ToScrapeRandomSpider(scrapy.Spider):
    name = "toscrape-random"
    start_urls = ["http://quotes.toscrape.com/random"]

    def parse(self, response):
        yield QuotesbotItem(
            text=response.css("span.text::text").get(),
            author=response.css("small.author::text").get(),
            tags=response.css("div.tags > a.tag::text").getall(),
        )

        # To get multiple random quotes, we can yield new requests to the same URL
        # Be careful not to create an infinite loop if not intended.
        # Here we'll just stop after one, or we could use a counter.
