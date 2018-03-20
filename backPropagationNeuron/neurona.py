import math

w1 = [[0.1,0.5],[-0.7,0.3]]
w2 = [[0.2],[0.4]]

tasaAprendizaje = 0.25

exits = []

def neuronError(total):
    print("Peso real: " + str(round(1-total,3)))

def exitLayerEntry():
    global exits
    exitEntry = w2[0][0]*exits[0] + w2[1][0]*exits[1]
    exitEntry = round(exitEntry,3)
    print("Entrada capa salida: " + str(exitEntry))
    return exitEntry

def exitLayer():
    net = exitLayerEntry()
    total = simoidalExit(net)
    neuronError(total)

def simoidalExit(net):
    global exits
    simoidal = 1 / (1 + (math.e ** (-(net))))
    simoidal = round(simoidal,3)
    exits.append(simoidal)
    print("Salida: " + str(simoidal))
    return simoidal

def hiddenLayerEntery(entryList,x1,x2):
    net = entryList[0]*x1 + entryList[1]*x2
    print("Entrada capa oculta: " + str(net))
    simoidalExit(net)

def hiddenLayer(x1,x2):
    global w1
    cont1 = 0
    cont2 = 0
    entryList = []
    while cont1 < len(w1):
        while cont2 < len(w1[cont1]):
            entryList.append(w1[cont2][cont1])
            cont2 += 1
        hiddenLayerEntery(entryList,x1,x2)
        entryList = []
        cont2 = 0
        cont1 += 1

def start(x1,x2,t1):
    hiddenLayer(x1,x2)
    exitLayer()

start(0,1,1)