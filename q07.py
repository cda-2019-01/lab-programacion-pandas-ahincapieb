##
## Agregue una columna  con la suma de _c0 y _c2 a la tabla tbl0.tsv 
## Leer archivo
x = pd.read_csv('tbl0.tsv', sep = '\t')
## Agregar columna
x.groupby(['_c1'])['_c2'].sum()

