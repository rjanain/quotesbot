import scrapy
from quotesbot.items import QuotesbotItem


class ToScrapeViewStateSpider(scrapy.Spider):
    name = "toscrape-viewstate"
    start_urls = ["http://quotes.toscrape.com/search.aspx"]

    def parse(self, response):
        # Extract quotes from the current page first
        for quote in response.css("div.quote"):
            yield QuotesbotItem(
                text=quote.css("span.text::text").get(),
                author=quote.css("small.author::text").get(),
                tags=quote.css("div.tags > a.tag::text").getall(),
            )

        # Demonstrate ViewState form submission
        # Check if there's a filter form (tag dropdown/input)
        if response.css('form select[name="tag"], form input[name="tag"]'):
            # Submit form with a tag filter using FormRequest.from_response
            # which automatically handles __VIEWSTATE and other hidden fields
            yield scrapy.FormRequest.from_response(
                response,
                formdata={"tag": "love"},
                callback=self.parse_filtered_results,
                dont_click=True,  # Don't simulate button click, just submit
            )

    def parse_filtered_results(self, response):
        # Parse filtered results
        for quote in response.css("div.quote"):
            yield QuotesbotItem(
                text=quote.css("span.text::text").get(),
                author=quote.css("small.author::text").get(),
                tags=quote.css("div.tags > a.tag::text").getall(),
            )
