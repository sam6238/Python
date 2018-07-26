# -*- coding: utf-8 -*-
import scrapy

#建立class繼承scrapy.Spide
class BooksSpider(scrapy.Spider):
    #建立唯一識別標籤
    name = 'books'
    #定義起點
    start_urls = ['http://books.toscrape.com/']

    #定義方法
    def parse(self, response):
        #透過css()方法->取得資料
        #分析網頁資料的標籤->取得各個「書」的資料->css('article.product_pod')
        #以遍歷方式
        for book in response.css('article.product_pod'):
            #取得書名跟價格
            #書名->article->h3->a->@title=>'./h3/a/@title'
            #extract_first()->只匹配第一個元素
            #使用xpath()路徑表達式
            name = book.xpath('./h3/a/@title').extract_first()
            #使用css()
            price = book.css('p.price_color::text').extract_first()
            #
            yield{
                'name':name,
                'price':price
            }
        
        #接著要往下一頁繼續爬->找到前往下一頁的url->href
        next_url = response.css('ul.pager li.next a::text(href)').extract_first()
        #假如有下一頁
        if next_url:
            #
            next_url = response.urljoin(next_url)
            #
            yield scrapy.Request(next_url, callback=self.parse)
        
    
