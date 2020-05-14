import csv
from datetime import date

day = date.today()

# Lista de municípios brasileiros e seus respectivos códigos IBGE.
with open('cidades.csv') as csv_file:
    csv_ibge = csv.reader(csv_file, delimiter=';')
    line = 0
    ibge_list = list()
    for row in csv_ibge:
        if line > 0:
            ibge_list.append(row)
        line += 1

''' 
    Lista com os dados climáticos (temperatura e umidade) de cada município brasileiro.
    city_list: Lista apenas os nomes dos municípios
    city_list_data: Lista com todos os dados climáticos por município
'''
with open('data.csv') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    line_count = 0
    city_list = list()
    city_list_data = list()
    for row in csv_reader:
        if line_count > 0:
            city_list.append(row[0])
            city_list_data.append(row)
        line_count += 1

new_city_list = list()

for data in city_list:
    a = [x.strip() for x in data.split(' - ')]
    new_city_list.append(a)

final_list = list()

# Obtém o código IBGE de cada município.

for row in new_city_list:
    for data in ibge_list:
        if row[0] == data[1] and row[1] == data[2]:
            final_list.append(data[0])

# Gera o arquivo no formato csv para ser usado no banco de dados
with open('dados_climaticos.csv', mode='w') as weather_file:
    weather_writer = csv.writer(weather_file, delimiter=';', quotechar='"', quoting=csv.QUOTE_ALL)

    for i in range(len(final_list)):
        if i == 0:
            weather_writer.writerow(['data', 'temp_max', 'temp_min', 'umidade_max', 'umidade_min', 'cod_mun'])
        else:
            weather_writer.writerow([day, city_list_data[i][2], city_list_data[i][1], city_list_data[i][4], city_list_data[i][3], final_list[i]])