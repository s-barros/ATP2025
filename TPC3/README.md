# Aplicação de listas
## Autor: Sara Barros, A111690
## Lista de resultados: 

```python
print('''(1) Criar Lista 
    (2) Ler Lista
    (3) Soma
    (4) Média
    (5) Maior
    (6) Menor
    (7) estaOrdenada por ordem crescente
    (8) estaOrdenada por ordem decrescente
    (9) Procura um elemento
    (0) Sair''')
op = int(input("escolha uma das seguintes opções: "))
res = []
import random

while op != 0:
    if op == 1:
        res = []
        elem = random.randint(1,20)
        i = 0
        while i < elem:
            num = random.randint(1,100)
            res.append(num)
            i = i + 1
        print(res)

    elif op == 2:
        res = []
        elem = int(input("quantos elementos é que quer que a sua lista tenha?"))
        i = 0
        while i < elem:
            num = int(input("escolha um número para adicionar a sua lista: "))
            res.append(num)
            i = i + 1
        print(res)

    elif op == 3:
        if res == []:
            print("Tem que escolher uma lista")
        else: 
            soma = 0
            i = 0
            while i < len(res)-1:
                soma = soma + res[i]
                i = i + 1
            print(soma)

    elif op == 4:
        if res == []:
            print("tem que escolher uma lista")
        else:
            soma = 0
            i = 0
            while i < len(res)-1:
                soma = soma + res[i]
                i = i + 1
            print(soma/len(res))

    elif op == 5:
        i = 0
        num = res[0]
        while i < len(res)-1:
            if res[i] > num:
                num = res[i]
            i = i + 1
        print(num)

    elif op == 6:
        i = 0
        num = res[0]
        while i < len(res)-1:
            if res[i] < num:
                num = res[i]
            i = i + 1
        print(num)

    elif op == 7:
        i = 0
        pres = "sim"
        while i < len(res)-1:
            if res[i] > res[i+1]:
                pres = "não"
            i = i + 1
        print(pres)

    elif op == 8:
        i = 0
        pres = "sim"
        while i < len(res)-1:
            if res[i] < res[i+1]:
                pres = "não"
            i = i + 1
        print(pres)

    elif op == 9:
        i = 0
        numproc = int(input("Que número é que procura?"))
        resp = -1
        while i < len(res)-1 and resp == -1:
            if numproc in res:
                resp = i
            i = i + 1
        print(resp)
        
        
    else:
        print("isso não faz parte das opções :(")

    print('''(1) Criar Lista 
    (2) Ler Lista
    (3) Soma
    (4) Média
    (5) Maior
    (6) Menor
    (7) estaOrdenada por ordem crescente
    (8) estaOrdenada por ordem decrescente
    (9) Procura um elemento
    (0) Sair''')
    op = int(input("escolha uma das seguintes opções: "))

print(res)
print("Até já")
```
