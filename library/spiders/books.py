import scrapy


class BookItem(scrapy.Item):
    title: scrapy.Field()
    price: scrapy.Field()
    amount_in_stock: scrapy.Field()
    rating: scrapy.Field()
    category: scrapy.Field()
    description: scrapy.Field()
    upc: scrapy.Field()


class BooksSpider(scrapy.Spider):
    name = "books"
    allowed_domains = ["books.toscrape.com"]
    start_urls = ["https://books.toscrape.com/"]

    def parse(self, response):
        pass
