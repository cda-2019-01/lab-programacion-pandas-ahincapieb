##
## Agregue una columna  con la suma de _c0 y _c2 a la tabla tbl0.tsv 
## Leer archivo
x = pd.read_csv('tbl0.tsv', sep = '\t')
## Agregar columna con la suma
x['suma'] = x['_c0'] + x['_c2']
x.head()

