# -*- coding: utf-8 -*-
"""
Created on Mon Feb 21 12:19:44 2022

@author: Asus
"""

import sqlite3
import json
import numpy as np
import pandas as pd

con = sqlite3.connect("./data/APIAY 04-10-21.db")

# Con la conexión, crea un objeto cursor
cur = con.cursor()

data = [];

for row in cur.execute('SELECT * FROM nodex;'):
    
    data.append(row[3]);
# No te olvides de cerrar la conexión
con.close()

titles = [
    'board_id',
    'device_id',
    'device_name',
    'hub_id',
    'sensor_count',
    'sensors',
    '10-salinity',
    '2-dissolved-oxygen',
    '3-tss-180',
    '4-tss-90',
    '5-temperature',
    '6-oil-water',
    '7-conductivity-AC',
    '8-conductivity-DC',
    '9-water-quality-index',
    'timestamp'
    ];

DataMatriz = np.zeros([len(data),len(titles)]);

data2=data[0];
respuestas=[];

for i in range(len(titles)):
    if i != len(titles)-1:
        title = titles[i];
        print(title)
        pos_ini=data2.find(titles[i]);
        pos_fin=data2.find(titles[i+1]);
        valor=data2[pos_ini+len(titles[i])+2:pos_fin-2]
        respuestas.append([valor]);
    else:
        valor=data2[pos_fin+len(titles[i])+2:-2]
        respuestas.append([valor]);
    
for j in range(len(data)-1):
    if j != len(data):
        dataRef = data[j+1];
        for i in range(len(titles)):
            if i != len(titles)-1:
                title = titles[i];
                print(title)
                pos_ini=dataRef.find(titles[i]);
                pos_fin=dataRef.find(titles[i+1]);
                valor=dataRef[pos_ini+len(titles[i])+2:pos_fin-2]
                respuestas[i].append(valor);
            else:
                valor=dataRef[pos_fin+len(titles[i])+2:-2]
                respuestas[i].append(valor);
                
df = pd.DataFrame()

for k in range(len(titles)):
    df[titles[k]] = respuestas[k];

df.to_excel('Nodex.xlsx');


