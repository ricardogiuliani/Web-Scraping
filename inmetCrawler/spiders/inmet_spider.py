import scrapy
import json
import pandas as pd
import csv
from datetime import date

codMunTodos = pd.read_csv('codMun.csv')
codMunTodos = codMunTodos['codMunIBGE'].values.tolist()

urls_api_inmet = []
data_inmet_list = []

for codigo in codMunTodos:
    string = 'https://apiprevmet3.inmet.gov.br/previsao/{}'.format(codigo)
    urls_api_inmet.append(string)


class InmetSpider(scrapy.Spider):
    name = "inmet_weather"

    def start_requests(self):
        for url in urls_api_inmet:
            yield scrapy.Request(url=url, callback=self.parse)

    def parse(self, response):
        jsonResponse = json.loads(response.text)
        
        codMun = list(jsonResponse.keys())
        codMun = codMun[0]
        
        dateToCrawl = list(jsonResponse[codMun].keys())
        dateToCrawl = dateToCrawl[0]

        tempMax = (jsonResponse[codMun][dateToCrawl]["tarde"]["temp_max"])
        tempMin = (jsonResponse[codMun][dateToCrawl]["noite"]["temp_min"])
        umi_max = (jsonResponse[codMun][dateToCrawl]["tarde"]["umidade_max"])
        umi_min = (jsonResponse[codMun][dateToCrawl]["tarde"]["umidade_min"])
        today = date.today()
        # print(urls_api_inmet)
        # COLOCAR COD MUN TODOS OS DADOSSSSS!!!!!!!!!!!
        
        with open(f'{today}.csv', 'a', newline='', encoding='utf-8') as csvfile:
            spamwriter = csv.writer(csvfile)
            spamwriter.writerow(['{};{};{};{};{};{}'.format(today,codMun,tempMin,tempMax,umi_max,umi_min)])

