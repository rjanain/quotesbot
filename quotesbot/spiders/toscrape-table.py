import scrapy
from quotesbot.items import QuotesbotItem


class ToScrapeTableSpider(scrapy.Spider):
    name = "toscrape-table"
    start_urls = ["http://quotes.toscrape.com/tableful"]

    def parse(self, response):
        # The tableful page has quotes in a table structure
        # Each row contains a quote with text, author, and tags
        # We use .quote class to select quote containers within the table

        for quote in response.css("div.quote"):
            yield QuotesbotItem(
                text=quote.css("span.text::text").get(),
                author=quote.css("small.author::text").get(),
                tags=quote.css("div.tags > a.tag::text").getall(),
            )

        # Pagination
        next_page = response.css("li.next > a::attr(href)").get()
        if next_page:
            yield scrapy.Request(response.urljoin(next_page))
