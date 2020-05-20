import scrapy
import w3lib.html



class InmetSpider(scrapy.Spider):
    name = 'tempo_inmet'
    url_list = open("/Users/ricardogiuliani/Scrapy/weather/weather/spiders/cities.txt")
    start_urls = ['http://www.inmet.gov.br/portal/index.php?r=tempo2/verProximosDias&code={code}'.format(code=code) for code in url_list.readlines()]

    def parse(self, response):
        city = w3lib.html.remove_tags(response.xpath('/html/body/div[3]/div[6]/div[1]/p').extract_first())
        temp = response.css('.knob::attr(value)').extract()
        max = temp[1]
        min = temp[0]
        umi_max = w3lib.html.remove_tags(response.xpath('//*[@id="quadro1_interno_dados_txt_umidade_max"]/p/b').extract_first())
        umi_max = umi_max[:2]
        umi_min = w3lib.html.remove_tags(response.xpath('//*[@id="quadro1_interno_dados_txt_umidade_min"]/p/b').extract_first())
        umi_min = umi_min[:2]

        

        yield {
                'cidade': city,
                'temp_max': max,
                'temp_min': min,
                'umi_max': umi_max,
                'umi_min': umi_min
        }