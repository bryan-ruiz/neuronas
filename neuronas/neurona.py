import math
print(math.e)

matrizError = []
matrizPesosSalida = []
x1,x2,s = "","",""
matrizPesosMebranaOculta = []
matrizPSalida = []
salidaObtenidaCapaSalida = 0
netCapaSalida, errorCapaSalida = 0,0
matrizResultadosNetosCapaOculta = []

def calcularSimoidal(net):
    print("}}+")
    print(net)
    return 1/1+(math.e**-(net))

def calcularSalidasCapaOculta():
    print("calcular salidas capa oculta")
    print(matrizResultadosNetosCapaOculta)
    contador = 0
    while contador < len(matrizResultadosNetosCapaOculta):
        contador2 = 0
        while contador2 < len(matrizResultadosNetosCapaOculta[contador]):
            print("calcular simou")
            print(matrizResultadosNetosCapaOculta[contador][contador2])
            #calcularSimoidal(matrizResultadosNetosCapaOculta[contador][contador2])
            contador2 += 1
        contador += 1

    matrizPSalida.append([2])
def calcularNetMembranaOculta():
    for i in matrizPesosMebranaOculta:
        resultadoNet = i[0]*x1 + i[1]*x2
        matrizResultadosNetosCapaOculta.append([resultadoNet])

def calcularNetMembranaSalida():
    global netCapaSalida
    contador = 0
    resultadoSuma = 0
    print("matrices")
    print(matrizPSalida)
    print(matrizPesosSalida)
    while contador < len(matrizPSalida):
        contador1 = 0
        while contador1 < len(matrizPesosSalida[contador]):
            resultadoSuma += float(matrizPSalida[contador]) * float(matrizPesosSalida[contador][contador1])
            contador1 += 1
        contador += 1
    netCapaSalida = 0# resultadoSuma

def calcularCapaOculta(salidaEsperada):
    calcularNetMembranaOculta()
    calcularSalidasCapaOculta()
    calcularErrorCapaOculta(salidaEsperada)


def calcularCapaSalida(esperado):
    global salidaObtenidaCapaSalida, netCapaSalida, errorCapaSalida
    netCapaSalida = calcularNetMembranaSalida()
    print("net capa salida")
    print(netCapaSalida)
    salidaObtenidaCapaSalida = calcularSimoidal(netCapaSalida)
    errorCapaSalida = calcularErrorCapaSalida(esperado)

def calcularErrorCapaOculta(salidaEsperada):
    cont1 = 0
    while(cont1 < len(matrizPesosMebranaOculta)):
        cont2 = 0
        while cont2 < len(matrizPesosMebranaOculta[cont1]):
            error = salidaEsperada - matrizPesosMebranaOculta[cont1][cont2]
            matrizError.append([error])
            cont2 += 1
        cont1 += 1

def calcularErrorCapaSalida(salidaEsperada):
    global salidaObtenidaCapaSalida
    return salidaEsperada - salidaObtenidaCapaSalida

def imprimir():
    print(matrizError)
    print(matrizPesosSalida)
    print(x1, " " ,x2," " , s)
    print(matrizPesosMebranaOculta)
    print(matrizPSalida)
    print(salidaObtenidaCapaSalida)
    print(netCapaSalida, " " ,errorCapaSalida)
    print(matrizResultadosNetosCapaOculta)

def ingresarPesosVariablesEntrada(valor1,valor2,valor3, peso1,peso2,peso3,peso4,psalida1, psalida2):
    global salidaEsperada, x1, x2
    x1 = valor1
    x2 = valor2
    salidaEsperada = valor3
    matrizPesosMebranaOculta.append([peso1, peso2])
    matrizPesosMebranaOculta.append([peso3, peso4])
    matrizPesosSalida.append([psalida1])
    matrizPesosSalida.append([psalida2])
    calcularCapaOculta(salidaEsperada)
    calcularCapaSalida(salidaEsperada)
    imprimir()

ingresarPesosVariablesEntrada(0,1,1,0.1,-0.7,0.5,0.3,0.2,0.4)