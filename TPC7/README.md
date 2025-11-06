# Teste de aferição
## Autor: Sara Belo Leal de Barros, A111690
## Resumo: resolução das questões propostas
## Lista de resultados: 

```python
#1.a)

lista1 = [1, 2, 3, 4, 5]
lista2 = [4, 5, 6, 7, 8]  
ncomuns = []
for a in lista1:
    if a not in lista2 and a not in ncomuns:
        ncomuns.append(a)
for a in lista2:
    if a not in lista1 and a not in ncomuns:
        ncomuns.append(a)
print(ncomuns)


#b)

texto = """Vivia há já não poucos anos algures num concelho do Ribatejo 
    um pequeno lavrador e negociante de gado chamado Manuel Peres Vigário"""
lista = []
listexto = texto.split(" ")
for a in listexto:
    if len(a) > 3:
        lista.append(a)
print(lista)


#c)

lista = ['anaconda', 'burro', 'cavalo', 'macaco']
listaRes = []
i = 0
while i < len(lista):
    elem = (i+1,lista[i])
    listaRes.append(elem)
    i = i + 1
print(listaRes)


#2.a)

def strCount(s, subs):
    i = 0
    n = 0
    while i <= len(s)-len(subs):
        if s[i:i+len(subs)] == subs:
            n = n + 1
        i = i + 1
    return n


#b)

def produtoM3(lista):
    novo = sorted(lista) 
    mul = novo[0]*novo[1]*novo[2]
    return mul


#c)

def reduxInt(n):
    
    while n >= 10:
        i = 0
        soma = 0
        s = str(n)
        while i < len(s):
            a = int(s[i])
            soma = soma + a
            i = i + 1 
        n = soma
    return soma


#d)

def myIndexOf(s1, s2):
    devolv = -1
    i = 0
    while i < len(s1) - len(s2) and devolv == -1:
        if s1[i : i + len(s2)] == s2:
            devolv = i
        i = i + 1
    return devolv


#3.a)

def quantosPost(redeSocial):
    print(len(redeSocial))
    return


#b)

def postsAutor(redeSocial, autor):
    i = 0
    post = []
    while i < len(redeSocial):
        if redeSocial[i]['autor'] == autor:
            post.append(redeSocial[i])
        i = i + 1 
    return post


#c)

def autores(redeSocial):
    autores = []
    for a in redeSocial:
        if a['autor'] not in autores:
            autores.append(a['autor'])
    autores.sort()
    return  autores


#d) 

def insPost(redeSocial, conteudo, autor, dataCriacao, comentarios):
    if len(redeSocial) == 0:
        id = "p1"
    else:
        id = "p" + str(int(redeSocial[-1]['id'][1:]) + 1)
    post = {'id':id,'conteudo': conteudo, 'autor':autor, 'dataCriacao':dataCriacao,'comentarios':comentarios}
    redeSocial.append(post)
    return redeSocial


#e)

def remPost(redeSocial, id):
    res = []
    i = 0
    while i < len(redeSocial):
        if redeSocial[i]['id'] != id:
            res.append(redeSocial[i])
        i = i + 1
    return res


#f) 

def postsPorAutor(redeSocial):
    i = 0
    res = {}
    while i < len(redeSocial):
        if redeSocial[i]['autor'] in res:
            res[redeSocial[i]['autor']] = res[redeSocial[i]['autor']] + 1
        if redeSocial[i]['autor'] not in res:
            res[redeSocial[i]['autor']] = 1
        i = i + 1
    return res


#g)

def comentadoPor(redeSocial, autor):
    i = 0
    res = []
    while i < len(redeSocial):
        n = 0
        stop = False
        while n < len(redeSocial[i]['comentarios']) and stop == False:
            if redeSocial[i]['comentarios'][n]['autor'] == autor:
                res.append(redeSocial[i])
                stop = True 
        i = i + 1 
    return res
```
