# Título
## Autor: nome, id, foto
## Resumo: lista de parágrafos
## Lista de resultados: links para os ficheiros da resolução

```python

def listar(cinema):
    res = []
    i = 0
    while i < len(cinema):
        res.append(cinema[i][-1])
        i = i + 1
    return res


def disponível(cinema, filme, lugar):
    disp = False
    i = 0
    if cinema[i][2] == filme and lugar <= cinema[i][0]:
        if cinema[i][2] == filme:
            if lugar not in cinema[i][1]:
                disp = True
        i = i + 1
    return disp


def listardisponibilidades(cinema):  
    i = 0
    while i < len(cinema):
        livres = cinema[i][0] - len(cinema[i][1])
        print(f"Filme: {cinema[i][2]} \nNum. de lugares livres: {livres}")
        i = i + 1


def inserirSala(cinema,sala):
    nlug = int(input("qual o número de lugares que esta sala tem?"))
    vend = []
    filme = input("Qual é o nome do filme? ")
    sala = [nlug, vend, filme]
    if sala not in cinema:
        cinema.append(sala)
    return cinema 


def vendebilhete(cinema,filme,lugar):
    i = 0
    while i < len(cinema):
        if cinema[i][2] == filme:
            if lugar not in cinema[i][1] and lugar <= cinema[i][0]:
                cinema[i][1].append(lugar)
                return(cinema[i][1])
        i = i + 1
    return(None)


#Menu

'''(1) Ver filmes
(2) Lugares disponíveis
(3) Compra de bilhete
(4) Dsiponiveis
(5) Criar Sala
(0) Sair''' 


#APP

sala1 = [120,[8,9,97,99,119],"Homem Aranha"]
sala2 = [100,[1,2,3,4],"Jumanji"]
sala3 = [50,[15,16,17],"O Rapaz e a Garça"]

cinema1 = [sala1,sala2,sala3]

op = input('''Olá :) O que vamos fazer hoje? (1) Ver filmes
(2) Lugares disponíveis
(3) Compra de bilhete
(4) Dsiponiveis
(5) Criar Sala
(0) Sair''')

while op != 0:
    if op == 1:
        print(listar(cinema1))
    elif op == 2:
        filme = input("Que filme quer ver?")
        lugar = int(input("Em que lugar é que gostaria de ficar?"))
        print(disponível(cinema1,filme,lugar))
    elif op == 3:
        filme = input("Que filme quer ver?")
        lugar = int(input("Em que lugar é que gostaria de ficar?"))
        print(vendebilhete(cinema1,filme,lugar))
    elif op == 4:
        print(listardisponibilidades(cinema1))
    elif op == 5:
        sala = input("Qual será o nome da nova sala?")
        print(inserirSala(cinema1,sala))

    op = input('''Olá :) O que vamos fazer hoje? (1) Ver filmes
    (2) Lugares disponíveis
    (3) Compra de bilhete
    (4) Dsiponiveis
    (5) Criar Sala
    (0) Sair''')

print("Bom filme!")

```



