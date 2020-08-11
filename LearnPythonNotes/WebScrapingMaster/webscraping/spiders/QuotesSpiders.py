import scrapy


'''CREATING A SPIDER
Spiders are classes that I define that Scrapy uses to scrape (extract) information from a website |s.
They must subclass scrapy.
They define the initial requests to make,

    SELECTORS
        CSS
        XPath


'''
# 
# 
# 
# 
# 
class QuoteSpyder(scrapy.Spider):
    name = 'quote'  # the name of the spider
    start_urls = [
        'https://bluelimelearning.github.io/my-fav-quotes/'  # I can add multipule websites.
    ]
    
    def parse(self, response):
        for quote in response.css('div.quotes'):
            yield {
                'quote':quote.css('p.aquote::text').extract(),
                'author':quote.css('p.author::text').extract_first(),
            }
    