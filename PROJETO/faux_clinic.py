# - Carrega na coleção do ficheiro para a memória
import json

def carregaBD(fnome):
    with open(fnome) as f:
        res= json.load(f)
    return res

# - Grava o ficheiro
def gravaBD(fnome, bd):
    with open(fnome, "w", encoding="utf-8") as f:
        json.dump(bd, f)
    return

# - Verifica as credenciais de um utilizador
def verificaUser(bd, id, pwd):
    res = None
    encontrado = False
    i = 0
    while not encontrado and i < len(bd):
        if id == bd[i]['id']:
            encontrado = True
            if pwd == bd[i]['password']:
                res = bd[i]
        i = i + 1
    return res

# adiciona os dados que o utilizador forneceu a simulação ao seu histórico

def aidicionahist(ficheiro, nome, dados):
    enc = False
    i = 0
    while i < len(ficheiro) and enc == False:
        if ficheiro[i]["user"].strip() == nome.strip(): #para evitar problemas com os espaços
            ficheiro[i]["historico"].append(dados) #neste momento só está a guardar os dados que a pessoa forneceu
            enc = True
        i = i + 1
    if enc == False:
        ficheiro.append({"user":nome,
                         "historico":[]})
        ficheiro[-1]["historico"].append(dados)
    return ficheiro

# lista o histórico do utilizador

def listahist(ficheiro, nome):
    for user in ficheiro:
        if user["user"].strip() == nome.strip():
            return user["historico"]
    return None