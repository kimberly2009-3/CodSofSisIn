with open('NOMBRES.txt','r') as fichero:
    for linea in fichero.readlines():
        print(linea, end='')