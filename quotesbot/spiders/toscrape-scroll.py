import json
import scrapy
from quotesbot.items import QuotesbotItem


class ToScrapeScrollSpider(scrapy.Spider):
    name = "toscrape-scroll"
    start_urls = ["http://quotes.toscrape.com/api/quotes?page=1"]

    def parse(self, response):
        data = json.loads(response.text)
        for quote in data["quotes"]:
            yield QuotesbotItem(
                text=quote["text"], author=quote["author"]["name"], tags=quote["tags"]
            )

        if data["has_next"]:
            next_page = data["page"] + 1
            yield scrapy.Request(
                url=f"http://quotes.toscrape.com/api/quotes?page={next_page}",
                callback=self.parse,
            )
