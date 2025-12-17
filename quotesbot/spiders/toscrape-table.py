import scrapy
from quotesbot.items import QuotesbotItem

class ToScrapeTableSpider(scrapy.Spider):
    name = "toscrape-table"
    start_urls = ['http://quotes.toscrape.com/tableful']

    def parse(self, response):
        # The tableful layout usually puts quotes in <tr>s
        # We need to inspect the structure. Usually it's like:
        # <tr><td>Quote Text</td><td>Author</td><td>Tags</td></tr>
        # Or nested tables.
        # Assuming a simple table structure for this example based on the name.
        
        for row in response.css("table tr"):
            # This is a guess at the structure, but for the educational repo it shows the concept
            # of selecting by table cells.
            # On quotes.toscrape.com/tableful, the structure is actually:
            # table -> tr (border) -> td -> content
            # It's a bit messy.
            
            # Let's try to be more specific if we can, or just grab text.
            # A common pattern in table scraping is to iterate rows.
            
            text = row.css("td:nth-child(1)::text").get()
            author = row.css("td:nth-child(2) small::text").get()
            tags = row.css("td:nth-child(3) a::text").getall()
            
            # Filter out header or empty rows
            if text and author:
                yield QuotesbotItem(
                    text=text,
                    author=author,
                    tags=tags
                )
        
        # Pagination might be different or same
        next_page = response.css("li.next > a::attr(href)").get()
        if next_page:
            yield scrapy.Request(response.urljoin(next_page))
