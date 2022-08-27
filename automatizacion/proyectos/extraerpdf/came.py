import camelot

sandia=camelot.read_pdf('','numpag')

print(sandia)

tabla.export('archivo.csv', f=csv, compress=True)
tabla[0].to_csv('archivo.csv')
