import scrapy
import w3lib.html


class WeatherSpider(scrapy.Spider):
    name = 'tempo'
    
    start_urls = ['https://www.climatempo.com.br/previsao-do-tempo/cidade/{city}'.format(city=city) for city in range(1, 6976)]

    def parse(self, response):
        city = w3lib.html.remove_tags(response.xpath('/html/body/div[3]/div[6]/div[3]/div[1]/div[3]/div[1]/p/span/text()').extract_first())
        min = w3lib.html.remove_tags(response.xpath('/html/body/div[3]/div[6]/div[3]/div[1]/div[3]/div[2]/div[1]/div[1]/div[1]/p[1]/span[2]').extract_first())
        max = w3lib.html.remove_tags(response.xpath('/html/body/div[3]/div[6]/div[3]/div[1]/div[3]/div[2]/div[1]/div[1]/div[1]/p[2]/span[2]').extract_first())
        umi_min = w3lib.html.remove_tags(response.xpath('//html/body/div[3]/div[6]/div[3]/div[1]/div[3]/div[2]/div[1]/div[1]/div[2]/ul[2]/li[3]/p/text()').extract_first())
        umi_max = w3lib.html.remove_tags(response.xpath('//html/body/div[3]/div[6]/div[3]/div[1]/div[3]/div[2]/div[1]/div[1]/div[2]/ul[3]/li[3]/p').extract_first())

        yield {
                'cidade': city,
                'temp_max': max,
                'temp_min': min,
                'umi_max': umi_max,
                'umi_min': umi_min
            }