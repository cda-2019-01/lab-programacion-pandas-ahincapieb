##
## Imprima la suma de la _c2 por cada letra de la _c1 
## de la tabla tbl0
## Leer archivo
x = pd.read_csv('tbl0.tsv', sep = '\t')
x.head()
## Impresion suma _c2
x.groupby('_c1').sum()['_c2']

