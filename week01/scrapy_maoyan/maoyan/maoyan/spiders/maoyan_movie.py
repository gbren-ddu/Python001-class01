import scrapy
from maoyan.items import MaoyanItem
from scrapy.selector import Selector


class MaoyanMovieSpider(scrapy.Spider):
    name = 'maoyan_movie'
    allowed_domains = ['maoyan.com']
    start_urls = ['http://maoyan.com/films?showType=3']

    def parse(self, response):
        if response.url != start_urls[0]:
            print("Please open '%s' in browser ！" % response.url)
            return
        # 获取电影列表
        tags = Selector(response=response).xpath(
            '//div[@class="movie-item-hover"]')

        print(len(tags), tags)
        
        count = 0
        for tag in tags:
            print(count)
            # 只取前10个电影
            if count >= 10:
                break

            # 电影名称的class和别的hover信息不同，可以直接通过class定位
            movie_title = tag.xpath(
                './/span[contains(@class,"name")]/text()').extract_first()
            print(movie_title)

            # 获取其它hover信息
            hover_texts = tag.xpath(
                './/span[@class="hover-tag"]/../text()').extract()
            # 通过xpath定位时多出了很多\n，数据索引有变化
            movie_type = hover_texts[1].strip('\n').strip()
            print(movie_type)
            movie_time = hover_texts[5].strip('\n').strip()
            print(movie_time)

            item = MaoyanItem()
            item['movie_title'] = movie_title
            item['movie_type'] = movie_type
            item['movie_time'] = movie_time

            count += 1
            yield item

