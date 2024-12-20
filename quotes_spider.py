import scrapy

class QuotesSpider(scrapy.Spider):
    name = "quotes"  # Name of the spider
    start_urls = [
        'http://quotes.toscrape.com/page/1/',  # Starting URL
    ]

    def parse(self, response):
        # Loop through each quote block
        for quote in response.css('div.quote'):
            # Extract text, author, and tags
            yield {
                'text': quote.css('span.text::text').get(),
                'author': quote.css('small.author::text').get(),
                'tags': quote.css('div.tags a.tag::text').getall(),
            }

        # Follow the "Next" page link if it exists
        next_page = response.css('li.next a::attr(href)').get()
        if next_page is not None:
            yield response.follow(next_page, self.parse)
