import os
import sys
import pandas as pd
import matplotlib as mpl
import matplotlib.pyplot as plt
import numpy
import seaborn as sns

DIR_OF_DATA = r'/home/julio/auto/aglt/mchn'
os.chdir(DIR_OF_DATA)

for txt in os.listdir():

    datas_mjd_rh = pd.read_csv(txt, sep='\s+', header=3, low_memory=False)
    parser_datas_rh = datas_mjd_rh['(2)']
    parser_datas_mjd = datas_mjd_rh['(15)']

    # Plotar MJD x RH
    MJD = parser_datas_mjd
    RH = parser_datas_rh

    # Plot(MJD x RH)
    fig, ax = plt.subplots(figsize=(5,4.5))
    plt.xlabel('MJD')
    plt.ylabel('RH')
    plt.title("MJD x RH")
    ax.scatter(MJD, RH, s=50, facecolor='C0', edgecolor='k')
