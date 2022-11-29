# Tratamento de Casas decimais
# Lendo as tabelas
# SNR está na coluna 8 --> Nomeada pelo número ==> 9
#Os nomes das colunas devem estar nos decimais
import os
import pandas as pd
from pandas import Series, DataFrame

wished_dir = r"/home/julio/auto/aglt/REFL_CODE/2019/snr/sph1"
os.chdir(wished_dir)

for csv in os.listdir():

    snr_data = pd.read_csv(csv, sep='\s+', low_memory=False)
    df_snr_log = DataFrame(data=snr_data)
    save_col_snr = df_snr_log.columns
    new_colsnr = save_col_snr[6]
    rounded_snr = Series([0], [new_colsnr])
    new_rounded_snr = df_snr_log.round(rounded_snr)
    #print(f'{csv}, {new_rounded_snr}')
    new_rounded_snr.to_csv(csv, index=False)
