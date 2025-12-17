# QuotesBot

This is a Scrapy project to scrape quotes from famous people from http://quotes.toscrape.com ([github repo](https://github.com/scrapinghub/spidyquotes)).

This project is only meant for educational purposes.

## About This Project

The [quotes.toscrape.com](http://quotes.toscrape.com) website is a scraping sandbox designed to teach web scraping techniques. It provides multiple endpoints, each demonstrating different challenges that modern web scrapers encounter:

- Basic HTML pages (CSS/XPath selectors)
- JavaScript-rendered content
- Infinite scroll with API backends
- Login-protected pages with CSRF tokens
- Table-based layouts
- Form submissions with ViewState
- Dynamic/random content endpoints

**QuotesBot provides working spider examples for all of these endpoints**, making it a complete learning companion for the quotes.toscrape.com sandbox. Each spider demonstrates the appropriate Scrapy techniques for handling its target endpoint's specific challenges.


## Extracted data

This project extracts quotes, combined with the respective author names and tags.
The extracted data looks like this sample:

    {
        'author': 'Douglas Adams',
        'text': '“I may not have gone where I intended to go, but I think I ...”',
        'tags': ['life', 'navigation']
    }


## Spiders
piders for each endpoint available on quotes.toscrape.com. You can list them using the `list` command:

    $ scrapy list
    toscrape-css
    toscrape-xpath
    toscrape-scroll
    toscrape-js
    toscrape-login
    toscrape-table
    toscrape-viewstate
    toscrape-random

Each spider targets a specific quotes.toscrape.com endpoint designed to teach different scraping techniques
Each spider targets a different endpoint or challenge on the website:

### Basic Spiders
- **`toscrape-css`** → `/` endpoint
  - Standard HTML scraping using CSS selectors
  - Best starting point for Scrapy beginners
  
- **`toscrape-xpath`** → `/` endpoint
  - Same endpoint as above but using XPath expressions
  - Learn alternative selector strategy

### JavaScript & API Endpoints
- **`toscrape-js`** → `/js/` endpoint
  - Extracts data from JavaScript-rendered pages
  - Parses JSON embedded in `<script>` tags as `var data = [...]`
  - Demonstrates reverse-engineering JS content
**Suggested progression through the quotes.toscrape.com endpoints:**

1. **Start with HTML basics**: 
   - `toscrape-css` and `toscrape-xpath` - Learn fundamental selectors
   
2. **Explore JavaScript & APIs**:
   - `toscrape-js` - Understand JS-rendered content
   - `toscrape-scroll` - Learn to use APIs directly
   
3. **Master authentication**:
   - `toscrape-login` - Handle login forms and sessions
   
4. **Tackle complex structures**:
   - `toscrape-table` - Parse table layouts
   - `toscrape-viewstate` - Handle stateful forms
   - `toscrape-random` - Work with dynamic content

Each spider is a complete, working example you can run, inspect, and modify. This hands-on approach with real endpoints helps you understand the techniques needed for production web scraping.
- **`toscrape-login`** → `/login` endpoint
  - Demonstrates form-based authentication flow
  - Uses `FormRequest.from_response()` for automatic CSRF token handling
  - Scrapes content only accessible after login
  
- **`toscrape-viewstate`** → `/search.aspx` endpoint
  - Handles ASP.NET ViewState forms
  - Extracts and submits hidden `__VIEWSTATE` fields
  - Teaches stateful form submissions for enterprise applications

### Complex Layouts
- **`toscrape-table`** → `/tableful/` endpoint
  - Parses quotes organized in HTML table structure
  - Iterates through table rows and extracts cell data
  - Demonstrates table scraping patterns
  
- **`toscrape-random`** → `/random` endpoint
  - Scrapes endpoint that returns different content each time
  - Handles dynamic/random content sources
### Learning Path

1. **Start with basics**: Run `toscrape-css` and `toscrape-xpath` to understand fundamental Scrapy concepts
2. **Progress to modern challenges**: Try the advanced spiders to learn techniques for:
   - Handling JavaScript-heavy websites
   - Working with APIs and JSON data
   - Managing authentication flows
   - Parsing complex layouts
   - Dealing with form-based navigation

You can learn more about Scrapy fundamentals by going through the
[Scrapy Tutorial](http://doc.scrapy.org/en/latest/intro/tutorial.html).

Learning

- **Explore each endpoint first**: Visit each URL in your browser to understand what you're scraping
  - Basic: `http://quotes.toscrape.com/`
  - JavaScript: `http://quotes.toscrape.com/js/`
  - Scroll/API: `http://quotes.toscrape.com/scroll/` (uses `/api/quotes?page=1`)
  - Login: `http://quotes.toscrape.com/login`
  - Table: `http://quotes.toscrape.com/tableful/`
  - ViewState: `http://quotes.toscrape.com/search.aspx`
  - Random: `http://quotes.toscrape.com/random`

- **Use browser DevTools**: Inspect the page source, network requests, and JavaScript to understand how each endpoint works

- **Compare approaches**: Run `toscrape-css` vs `toscrape-xpath` on the same endpoint to see different selector strategies

- **Check API responses**: For `toscrape-scroll`, visit the API endpoint directly to see the JSON structure

- **Experiment freely**: quotes.toscrape.com is a sandbox designed for learning - modify the spiders and try different technique
```
cd quotesbot
pip install scrapy
```

## Running the spiders

You can run a spider using the `scrapy crawl` command, such as:

    $ scrapy crawl toscrape-css

If you want to save the scraped data to a file, you can pass the `-o` option:
    
    $ scrapy crawl toscrape-css -o quotes.json

### Example Commands

```bash
# Basic scraping with CSS selectors
scrapy crawl toscrape-css -o quotes-css.json

# Scrape JavaScript-rendered content
scrapy crawl toscrape-js -o quotes-js.json

# Scrape with authentication
scrapy crawl toscrape-login -o quotes-login.json

# Scrape using API (infinite scroll)
scrapy crawl toscrape-scroll -o quotes-scroll.json

# Scrape from table layout
scrapy crawl toscrape-table -o quotes-table.json
```

## Tips for Students

- **Compare CSS vs XPath**: Run both `toscrape-css` and `toscrape-xpath` to see different selector strategies
- **Inspect the target websites**: Use browser DevTools to understand page structure before writing selectors
- **Check the API**: For `toscrape-scroll`, visit `http://quotes.toscrape.com/api/quotes?page=1` in your browser to see the JSON structure
- **Authentication testing**: The login credentials for `toscrape-login` are typically test credentials provided by the site
- **Experiment safely**: This sandbox is designed for learning, so feel free to modify and experiment with the spiders
