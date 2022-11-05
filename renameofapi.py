##########################################################################################
# ROTINA QUE RENOMEIA ARQUIVOS A PARTIR DE INFORMARÇÕESDE API IURI - DADOS_6_DIGITOS.LOG #
#########################################################################################
import os
from datetime import datetime

# Constantes
wished_dir = r"/home/julio/auto/dados_brutos/"
# 1 - wished_dir = input('r"/Caminho da pasta/"')
os.chdir(wished_dir)

"""
Estação geodeśica é informada pelo usuário, deve ser informada
com 4 caracteres str obrigatoriamente:
Exemplo:
a) Estação geodésica IBGE: ibge ou ibg1
"""
station = str(input('name of station with four digites: '))

ncery_type = '0' # Dígito Zero, obrigatório devido à convensão geodésica para gzip e gnssrefl
extension_gzip = '.A' # Extensão de gzip

for f in os.listdir():

    # Desempacota nome do arquivo atual
    f_name, f_ext = os.path.splitext(f)
    f_data = f_name.split()
    f_year, f_month, f_day = f_data[0][0:2], f_data[0][2:4], f_data[0][4:6]
    compdt = f_year + '-' + f_month + '-' + f_day
    year_universal_day = f_year + '-' + '01' + '-' + '01' # Primeiro dia do ano


    """
    Configurando dígito 0 necessário para o dia corrido do gzip
    Dia corrido do ano - a) 0 a 9 dias; b) 11 a 99 dias; c) 100 a 366 dias
    a) stat0010 - 1 dia equivalente ao 1° dia do ano
    b) stat0110 - 11 dias equivalente ao 11° dia do ano
    c) stat1100 - 110 dias equivalente ao 110° dia do ano
    """

    # Cálcula os dias corridos do ano - 01/01/20yy até dia dd/mm/20yy do mesmo ano
    dt2 = datetime.strptime(compdt, '%y-%m-%d')
    dt1 = datetime.strptime(year_universal_day, '%y-%m-%d')

    # Datas com três dígitos - saída esperada: 3650 (365° dia do ano)
    if len(str(abs((dt2 - dt1).days))) == 3 :
        sequential_day = str(abs((dt2 - dt1).days)) + '0'

    # Datas com dois dígitos - saída esperada: 0310 (31° dia do ano)
    elif len(str(abs((dt2 - dt1).days))) == 2 :
        sequential_day = '0' + str(abs((dt2 - dt1).days)) + '0'

    # Datas com 1 dígito - saída esperada: 0090 (9° dia do ano)
    elif len(str(abs((dt2 - dt1).days))) <= 1:
        sequential_day = '0' + f_day + '0'

    #Compõe nome final do arquivo - extensão gzip, solicitada pelo pacote processador
    compname_nmea = station + sequential_day + '.' + f_year + extension_gzip

    # Renomear arquivo para o gzip exigido
    os.rename(f, compname_nmea)
    #print(f'|||||---> {gzip_file_nmea} <---|||||')


"""
A) Concatenar as informações de acordo com a nomenclatura exigida:
Nome aceito: ABCD0030.21.A
- ABCD --> estação
- 0030 --> dia 3, ou 3° dia do ano + dígito 0
    * Criar uma lógica para calcular o dia corrido do ano?
- .21  --> ano
- .A   --> Extensão gzip
"""
