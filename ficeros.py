fs = open('prueba.csv', 'w')

fs.write('id,venta,comprar \n')

for i in range(100):
    fs.write(f'{i+1},3.40,2.30 \n')

