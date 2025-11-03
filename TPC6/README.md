# App meteorológica
## Autor: Sara Belo Leal de Barros, A111690.
## Resumo: Aplicação criada no vscode para fazer várias operações meteorológicas
## Lista de resultados: 

```python
tabMeteo1 = [((2022,1,20), 2, 16, 0),((2022,1,21), 1, 13, 0.2), ((2022,1,22), 7, 17, 0.01)]

#Funções:

#1
def medias(tabMeteo):
    res = []
    for i in tabMeteo:
        res.append((i[0],(i[1]+i[2])/2))        
    return res

#2
def guardaTabMeteo(t, fnome):
    f = open(fnome, "w")
    for i in t:
        f.write(f"{i[0][0]};{i[0][1]};{i[0][2]};{i[1]};{i[2]};{i[3]}\n")
    f.close()
    return

#3
def carregaTabMeteo(fnome):
    f = open(fnome, encoding='utf-8')
    res = []
    for linha in f: 
        campos = linha.split(";")
        res.append(((int(campos[0])),(int(campos[1])),(int(campos[2])),(float(campos[3])),(float(campos[4])),(float(campos[5]))))
    f.close()
    return res

tabMeteo2 = carregaTabMeteo("meteorologia.txt")

#4
def minMin(tabMeteo):
    minima = tabMeteo[0][1]
    for dia in tabMeteo[1:]:
        if dia[0][1] < minima:
            minima = dia[0][1]
    return minima

#5
def amplTerm(tabMeteo):
    res = []
    i = 0
    while i < len(tabMeteo):
        amp = tabMeteo[i][2]-tabMeteo[i][1]
        cena = (tabMeteo[i][0],amp)
        res.append(cena)
        i = i + 1
    return res

#6
def maxChuva(tabMeteo):
    i = 1
    um = tabMeteo[0][3]
    dia = tabMeteo[0][0]
    while i < len(tabMeteo):
        if tabMeteo[i][3] > um:
            um = tabMeteo[i][3]
            dia = tabMeteo[i][0]
        i = i + 1
    return (dia, um)

#7
def diasChuvosos(tabMeteo, p):
    res = []
    i = 0
    while i < len(tabMeteo):
        if tabMeteo[i][3] > p:
            cena = (tabMeteo[i][0],tabMeteo[i][3])
            res.append(cena)
        i = i + 1
    return res

#8
def maxPeriodoCalor(tabMeteo, p):
    i = 0
    n = 0
    nmaior = 0
    while i < len(tabMeteo):
        if tabMeteo[i][3] < p:
            n = n + 1
        else:
            if n > nmaior:
                nmaior = n
            n = 0
        i = i + 1
    if n > nmaior:
        nmaior = n  
    return nmaior

#9
import matplotlib.pyplot as plt

def extraiTMin(t):
    res = []
    for _,tmin,_,_ in t:
        res.append(tmin)
    return res 

def extraiTmax(t):
    res = []
    for _,_,tmax,_ in t:
        res.append(tmax)
    return res

def extraiPrecip(t):
    res = []
    for _,_,_,precip in t:
        res.append(precip)
    return res

def grafTabMeteo(t):

    x1 = list(range(1, len(t)+1))
    y1 = extraiTMin(t)
    plt.plot(x1, y1, label = "T mínima")
 
    x2 = list(range(1, len(t)+1))
    y2 = extraiTmax(t)
    plt.plot(x2, y2, label = "T máxima")

    x3 = list(range(1, len(t)+1))
    y3 = extraiPrecip(t)
    plt.plot(x3, y3, label = "precipitação")
 
    plt.xlabel('Dias')

    plt.ylabel('Dados')

    plt.title('Gráfico da Tmin, Tmáx e precipitação')
    plt.legend()
    plt.show()

    return


#App:

op = int(input("""Olá :) O que vamos fazer hoje?
                1) Tmédia em cada dia; 
               2) guarda tabela meteorológica em ficheiro; 
               3) carregar tabela de um ficheiro; 
               4) Tmin. registada 
               5) Amp térmica de cada dia; 
               6) dia com p máx; 
               7) dias em que a precipitação foi maior do que p; 
               8) maior número consecutivo de dias com precipitação inferior a p; 
               9) gráf de Tmin, Tmáx e p.
               0) Sair"""))

while op != 0:
    if op == 1:
        print(medias(tabMeteo1))
    if op == 2:
        guardaTabMeteo(tabMeteo1, "meteorologia.txt")
    if op == 3:
        print(len(tabMeteo2),tabMeteo2)
    if op == 4:
        print(minMin(tabMeteo1))
    if op == 5:
        print(amplTerm(tabMeteo1))
    if op == 6:
        print(maxChuva(tabMeteo1))
    if op == 7:
        p = float(input("Qual é o valor de p que vamos testar?"))
        print(diasChuvosos(tabMeteo1,p))
    if op == 8:
        p = float(input("Qual é o valor de p que vamos testar?"))
        print(maxPeriodoCalor(tabMeteo1,p))
    if op == 9:
        grafTabMeteo(tabMeteo1)

    op = int(input("""Olá :) O que vamos fazer hoje?
                1) Tmédia em cada dia; 
               2) guarda tabela meteorológica em ficheiro; 
               3) carregar tabela de um ficheiro; 
               4) Tmin. registada 
               5) Amp térmica de cada dia; 
               6) dia com p máx; 
               7) dias em que a precipitação foi maior do que p; 
               8) maior número consecutivo de dias com precipitação inferior a p; 
               9) gráf de Tmin, Tmáx e p.
               0) Sair"""))

print("Até já :)")
```
