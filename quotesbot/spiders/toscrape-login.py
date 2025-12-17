import scrapy
from quotesbot.items import QuotesbotItem


class ToScrapeLoginSpider(scrapy.Spider):
    name = "toscrape-login"
    login_url = "http://quotes.toscrape.com/login"
    start_urls = [login_url]

    def parse(self, response):
        # Submit the login form
        # CSRF token is handled automatically by FormRequest.from_response if it's in a hidden field
        return scrapy.FormRequest.from_response(
            response,
            formdata={"username": "myuser", "password": "mypassword"},
            callback=self.after_login,
        )

    def after_login(self, response):
        # Check if login succeeded
        if "Logout" in response.text:
            self.logger.info("Login successful!")
            # Now scrape the quotes
            for quote in response.css("div.quote"):
                yield QuotesbotItem(
                    text=quote.css("span.text::text").get(),
                    author=quote.css("small.author::text").get(),
                    tags=quote.css("div.tags > a.tag::text").getall(),
                )

            next_page = response.css("li.next > a::attr(href)").get()
            if next_page:
                yield scrapy.Request(
                    response.urljoin(next_page), callback=self.after_login
                )
        else:
            self.logger.error("Login failed")
