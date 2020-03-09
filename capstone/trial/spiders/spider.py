import scrapy



class QuotesSpider(scrapy.Spider):
    name = "crawling"
    start_urls = [
        'https://blog.griddynamics.com/explore/'
    ]

    def parse(self, response):
        for article in response.css('div.explor'):
            yield {
                'article_name': article.css('div > h4 > a::text').get(),
                'author': article.css('div > div > div > a::text').getall(),
                'link': article.css(' div > h4 > a::attr(href)').get(),
                'date': article.css('div > div > div.authwrp > span::text').get(),
                'tags': article.css('div > span > span > a::text').getall()
            }
