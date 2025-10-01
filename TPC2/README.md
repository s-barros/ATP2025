# TPC1: Jogo dos fósforos

<div style="display: flex; align-items: center; justify-content: center">
  <img src="TPC1/imagens/eu.jpg" alt="foto" width="148.8"/>
</div>

## Autor: Sara Belo Leal de Barros, A111690 
## Resumo: Jogo dos fósforos feito no vscode em python.  
## Lista de resultados: 

```python
jogador = input("Olá! Queres ser o primeiro ou o segundo jogador? (1 ou 2) ")
import random
numcomp = random.randint(1, 4)  
fosf = 21

while fosf > 1:
    if jogador == "1":
        num = int(input("Escolhe um num de fosforos para tirar: (1 a 4) "))
        fosf = fosf - num 
        print(fosf)
        ultimo = jogador
        if fosf > 1:
            if num == 1:
                numcomp = 4
            elif num == 2:
                numcomp = 3
            elif num == 3:
                numcomp = 2
            else:
                numcomp = 1
        
            fosf = fosf - numcomp
            print(fosf)
            ultimo = "computador"
    
    else:
        fosf = fosf - numcomp
        print(fosf)
        ultimo = "computador"
        if fosf > 1:
            num = int(input("Escolhe um num de fosforos para tirar: (1 a 4) "))
            fosf = fosf - num 
            print(fosf)
            ultimo = jogador
            if num + numcomp < 5:
                if num + numcomp == 2: 
                    numcomp = 3
                if num + numcomp == 3:
                    numcomp = 2
                else:
                    numcomp = 1
            elif num + numcomp > 5:
                if num + numcomp == 6:
                    numcomp = 4
                if num + numcomp == 7:
                    numcomp = 3
                else:
                    numcomp = 2
            else:
                numcomp = random.randint(1, 4)

print("fim")       
print("Ganhou :",ultimo)
```







