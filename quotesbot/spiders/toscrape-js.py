import json
import re
import scrapy
from quotesbot.items import QuotesbotItem


class ToScrapeJSSpider(scrapy.Spider):
    name = "toscrape-js"
    start_urls = ["http://quotes.toscrape.com/js/"]

    def parse(self, response):
        script_data = response.xpath(
            '//script[contains(text(), "var data =")]/text()'
        ).get()
        if script_data:
            # Extract the JSON list from the script text
            match = re.search(
                r"var data = (\[.*?\]);", script_data, re.DOTALL
            )
            if match:
                json_str = match.group(1)
                data = json.loads(json_str)
                for quote in data:
                    yield QuotesbotItem(
                        text=quote["text"],
                        author=quote["author"]["name"],
                        tags=quote["tags"],
                    )

        # Pagination for JS page usually follows the same pattern or links
        # But on the JS page, the "Next" button is also JS generated.
        # However, the URL structure /js/page/2/ usually works or we can find the link in the data if present.
        # For this example, let's assume we just want to show how to extract data from the script.
        # If we want pagination, we might need to check if the script has 'next' info or just increment page number.
        # Let's check if there is a next page link in the HTML (often there is a <li class="next"> even if hidden or generated).
        # Actually, on quotes.toscrape.com/js, the pagination links are normal <a> tags but the content is JS.

        next_page = response.css("li.next > a::attr(href)").get()
        if next_page:
            yield scrapy.Request(response.urljoin(next_page))
