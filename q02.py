##
## Imprima el promedio de la _c2 por cada letra de la _c1 
## de la tabla tbl0
import pandas as pd
## Lectura de la tabla 
x = pd.read_csv('tbl0.tsv', sep = '\t')
##
## Promedio de la _c2 por cada letra de la _c1
x.groupby('_c1').mean()['_c2']

