import heapq
import random
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import json

TEMPO_MEDIO_ATENDIMENTO = 2 
DISTRIBUICAO_TEMPO_ATENDIMENTO = "exponential"
TEMPO_MEDIO_CONSULTA = 15
DISTRIBUICAO_TEMPO_CONSULTA = "exponential"

CHEGADA = "chegada"
FIM_ATENDIMENTO = "atendimento"
SAIDA = "saída"

def gera_tempos_chegada(): #função que gera a lista dos tempos de chegada dos pacientes
    taxas = [
        (0, 4 * 60, 5 / 60),   # primeiras 4 horas - chegam 5 doentes por hora
        (4 * 60, 5 * 60, 15 / 60),  # horas 4 e 5, expediente normal, chegam 15/hora
        (5 * 60, 6 * 60, 30 / 60),  # horas de ponta, chegam 30/hora
        (6 * 60, 8 * 60, 15 / 60)   # horas restantes o fluxo volta ao normal
        ]
    # taxas = [(hinicio,hfim,taxa),...]
    tchegadas = []
    tempo_atual = 0.0

    for hinicio, hfim, taxa in taxas: #hinicio corresponde ao tempo registado em que se começa a aplicar uma determinada taxa; hfim quando deixamos de aplicar a taxa;taxa qual é a taxa de chegada dos pacientes.
        tempo_atual = hinicio #estabelece o tempo atual como se fosse o tempo em que a taxa começou a ser aplicada
        fim = False
        while not fim:
            intervalo = np.random.exponential(1 / taxa) #gera um intervalo entre este doentes e o próximo a partir da taxa de chegada dos pacientes e de uma distribuição exponencial o que faz variar o intervalo fazendo com que ele não tenha sempre o mesmo valor
            tempo_atual += intervalo #atualização do tempo atual 
            if tempo_atual > hfim: 
                fim = True # O período desta taxa chegou ao fim
            tchegadas.append(tempo_atual) #adiciona o tempo de chegada de um doente a lista de chegadas
    return tchegadas

#Events = [] #queue de eventos com base nos tempos de chegada
def pacientes_tchegadas(tchegadas, pessoas = 'pessoas.json'): #função atribui pacientes às chegadas
    Events = [] #lista para onde vão todos os eventos de chegada quando estiverem com uma pessoa associada ao tempo de chegada
    f = open( pessoas, 'r', encoding= 'utf-8') #o encoding está aqui para evitar problemas entre sistemas operativos
    pessoas = json.load(f) 
    pessoas_escolhidas = [] #lista auxiliar para onde vão as pessoas que são escolhidas a partir do ficheiro pessoas
    for t in tchegadas:
        if Events == []: #caso a lista esteja vazia não precisa se preocupar com twins 
            i = random.randint(0, len(pessoas)-1) # gera uma posição aleatória. temos que retirar 1 porque nesta função o limite superior conta
            paciente = pessoas[i] # a pessoa dessa posição aleatória vira paciente
            e = [t, CHEGADA, '', paciente['nome'], paciente['idade']] # nosso evento e descrito assim, sendo que paciente ainda não tem id 
            pessoas_escolhidas.append(paciente) # adiciona na lista de pessoas_escolhidas 
            Events.append(e) # adiciona o evento a lista de Events -> p q não queueEventos ?
        else:
            i = random.randint(0, len(pessoas)-1) # gera uma posição aleatória
            paciente = pessoas[i]  # a pessoa dessa posição aleatória vira paciente 
            if paciente in pessoas_escolhidas: # se a pessoa escolhida já esteja entre as pessoas escolhidas
                while paciente in pessoas_escolhidas: # enquanto isso acontecer geramos novos pacientes aleatórios
                    i = random.randint(0, len(pessoas)-1)
                    paciente = pessoas[i]
                pessoas_escolhidas.append(paciente)
            else: # quando finalmente não é um twin, adicionamos 
                pessoas_escolhidas.append(paciente)
            e = [t, CHEGADA, '', paciente['nome'], paciente['idade']] #criação do evento. o campo vazio é para onde vai o id do paciente
            Events.append(e) #adiciona o evento a lista
    return Events



def especialidade_doente(Events): #função para atribuição de uma especialidade para o doente ser tratado
    especialidades = {'Clinica Geral': (1, 20), 'Ortopedia': (21, 28), 'Dermatologia': (29, 44), 'Cardiologia': (45, 60)} # definimos uma probabilidade p/ especialidade
    especialidades_criança = 'Pediatria' # se for criança, automaticamente é pediatria
    for e in Events: #Evento = [tempo: Float, tipo: String, doente: String, idade: int, especialidade: String, gravidade: String] falta o id neste modelo, mas ele existe no evento pode é estar ainda vazio
        idade = e[4]
        if idade < 18: #se for criança a especialidade atribuida é automáticamente pediatria
            esp = especialidades_criança
        else: 
            i = random.randint(1, 60) #escolhe um número aleatório para determinar a especialidade dependendo do intervalo em que o número se insere
            for espe in especialidades:
                if especialidades[espe][0] <= i <= especialidades[espe][1]: # se i estiver entre os extremos da especialidade, esta é a especialidade do doente
                    esp = espe
        e.append(esp) #adiciona a especialidade ao evento do paciente
    return Events

def gravidade_doente(Events):  #função que atribui uma gravidade ao evento do paciente                                                     
    for e in Events: 
        i = random.randint(1, 100) #escolhe um número aleatório
        if 1 <= i <= 88: # uso da mesma lógica vista em especialidade
            gravidade = 'Baixa'
        elif 89 <= i <= 98:
            gravidade = 'Média'
        else:
            gravidade = 'Alta'
        e.append(gravidade) #adiciona a gravidade ao evento 
    return Events

# --- Modelo para o evento
# Evento = [tempo: Float, tipo: String, id: string, doente: String, idade: int, especialidade: String, gravidade: String]
# --- Funções de manipulação
def e_tempo(e): #para saber qual é o tempo do evento
    return e[0]

def e_tipo(e): #para saber de que tipo é o evento
    return e[1]

def e_id(e): #para saber o id do paciente
    return e[2]

def e_doente(e): #para saber o nome do paciente
    return e[3]

def e_idade(e): #para saber a idade do paciente
    return e[4]

def e_especialidade(e): #para saber a especialidade do evento
    return e[5]

def e_gravidade(e): #para saber a gravidade do evento
    return e[6]
# ---
# --- Modelo para a Queue de Eventos
# queueEventos = [Evento]
# --- Funções de manipulação

def procuraPosQueue(q, t): #permite descobrir em que posição é que um evento deverá estar de acordo com o seu tempo (a lista deverá estar por ordem cronológica)
    i = 0
    while i < len(q) and t > q[i][0]:
        i = i + 1
    return i

def enqueue(q, e): #função para colocar alguém na queue
    pos = procuraPosQueue(q, e[0]) #descobre em que posição a pessoa deveria ficar para que a lista fique por ordem cronológica
    return q[:pos] + [e] + q[pos:] #devolve a nova queue com o evento inserido de forma a lisyta se manter ordenada


def dequeue(q): #função que recebe a lista de eventos e remove o evento da lista de acordo com a idade do paciente ou pela ordem de chegada
    for i, evento in enumerate(q): # pecorre q e informa o indice de cada evento
        if evento[4] >= 65:  # verifica a idade
            e = q.pop(i) # .pop remove o elemento pelo indice, pode ser remove(), mas ai remove pelo evento
            return e, q # retorna o evento retirado e a fila atualizada
    # se nenhum tem idade >= 65, retorna o primeiro da fila
    e = q.pop(0)
    return e, q


#modelo queueConsulta = [(Cardiologia, []), (ortopedia, []), (Dermatologia, []), (Clinica Geral, []) ,(Pediatria, [])]

def enqueue2(e, queueConsulta): #adiciona um evento a queue passada como argumento
    for esp, fila in queueConsulta: #vai ver as queues que as queues de consulta tem 
        if e[5] == esp: #se a especialidade do evento corresponder a especialidade da fila de espera ele é adicionado a essa fila
            fila.append(e) 
    return queueConsulta # função retorna a fila atualizada 

def dequeue2(q,espm): #remove um evento da queue da especialidade do evento de acordo com a gravidade do evento
    for esp,fila in q: #para ver a especialidade e a fila de espera dessa especialidade
        if esp == espm and fila != []: #se a especialidade da fila coincidir com a especialidade passada como argumento e se essa fila não estiver vazia vamos começar a remover um evento
            i = 0
            enc = False
            while i < len(fila) and enc == False:
                if e_gravidade(fila[i]) == 'Alta': #ao encontrar um evento grave ele é automaticamente removido. Se chegar ao final da fila sem encontrar um evento grave ele passa para o ciclo seguinte para verificar se existem eventos de gravidade menor
                    e = fila[i]
                    fila.pop(i)
                    enc = True
                    return e, q
                i = i + 1 
            i = 0
            while i < len(fila) and enc == False:
                if e_gravidade(fila[i]) == 'Média': #mesma coisa que o de cima, mas a gravidade é menor
                    e = fila[i]
                    fila.pop(i)
                    enc = True
                    return e, q
                i = i + 1
            i = 0
            while i < len(fila) and enc == False: #remove o primeiro evento de baixa gravidade que encontrar
                if e_gravidade(fila[i]) == 'Baixa':
                    e = fila[i]
                    fila.pop(i)
                    enc = True
                    return e, q
                i = i + 1
    return None, q
                


#modelo para a rececionista (ou o)
# rececionista = [id: String, ocupado: Boolean, doente_corrente: String, total_tempo_ocupado: Float, inicio_ultima_consulta: Float]
#funções:

def r_id(e): #para saber o id do rececionista
    return e[0]

def r_ocupado(e): #para saber se está ocupado ou não
    return e[2]

def r_ocupado(e,rlista): #para saber se está ocupado
    for rececionista,_,paciente,_,_ in rlista:  #vai a lista de recionistas e verifica os seus dados         
        if rececionista == e: #se a rececionista for igual a passada como argumento
            if paciente is not None: # se tiver um paciente ele está ocupado 
                return True
    return False #caso contrário não está

def rOcupa(r): 
    r[1] = not r[1] # altera o campo ocupado pelo valor inverso
    return r

def r_doente_corrente(e): #diz qual o doente que está a atender
    return e[2]

def rDoenteCorrente(r, d): #atualiza o doente que a rececionista está a atender
    r[2] = d
    return r

def r_total_tempo_ocupado(r): #para ver quanto tempo é que o rececionista esteve ocupado
    return r[3]

def rTempoOcupado(r, t): #atualiza o tempo ocupado
    r[3] = t
    return r

def r_inicio_ultima_rececao(r): #vê quando é que a rececionista começou a atender alguém na última vez
    return r[4]

def rInicioRececao(r, t): #atualiza o tempo do último atendimento
    r[4] = t
    return r

def procuraRececionista(lista): # procura uma rececionista livre
    res = None
    i = 0
    encontrado = False
    while not encontrado and i < len(lista):
        if not lista[i][1]:
            res = lista[i] #atualiza res para que passe a ser igual a rececionista que está livre
            encontrado = True #encontrou uma rececionista livre
        i = i + 1
    return res #se não houver rececionistas livres vai retornar none

#Modelo para atendimento 

def gera_tempo_atendimento(): #gera o tempo que o atendimento vai demorar de acordo com o tipo de distribuição que foi passada como parâmetro
    if DISTRIBUICAO_TEMPO_ATENDIMENTO == "exponential":
        return np.random.exponential(TEMPO_MEDIO_ATENDIMENTO)
    elif DISTRIBUICAO_TEMPO_ATENDIMENTO == "normal":
        return max(0, np.random.normal(TEMPO_MEDIO_ATENDIMENTO, 5))
    elif DISTRIBUICAO_TEMPO_ATENDIMENTO == "uniform":
        return np.random.uniform(TEMPO_MEDIO_ATENDIMENTO * 0.5, TEMPO_MEDIO_ATENDIMENTO * 1.5)


# --- Modelo para o médico
# Médico = [esp: String, id: String, sala: String, ocupado: Boolean, doente_corrente: String, total_tempo_ocupado: Float, inicio_ultima_consulta: Float]

# --- Funções de manipulação
def m_id(e): #id do médico
    return e[0]

def m_ocupado(e): #se está ocupado ou não
    return e[1]

def m_ocupado(e,mlista): #se está ocupado ou não
    for _,medico,_,_,paciente,_,_ in mlista: #procura o medico na lista de medicos
        if medico == e: #se o médico coincidir com o que foi passado como argumento
            if paciente is not None:
                return True #se está ocupado
    return False #se não está ocupado

def mOcupa(m): #altera o estado de ocupação do médico
    m[3] = not m[3]
    return m

def m_doente_corrente(m): #qual é o doente que o médico está a atender
    return m[2]

def mDoenteCorrente(m, d): #atualiza o doente que está a ser atendido
    m[2] = d
    return m

def m_total_tempo_ocupado(m): #quanto tempo é que o médico esteve ocupado
    return m[3]

def mTempoOcupado(m, t): #atualiza o tempo ocupado
    m[3] = t
    return m

def m_inicio_ultima_consulta(e): #verifica quando é que a última consulat começou
    return e[4]

def mInicioConsulta(m, t): #atualiza o tempo da última consulta
    m[4] = t
    return m

def m_esp(m): #procura a especialidade do médico
    return m[5]

def medico_atend(m, queueConsulta): #faz com que o médico passe a atender um novo paciente se houver pacientes para atender
    if m[3] == False: #se o médico não estiver ocupado
        for esp, fila in queueConsulta: #vai ver se há gente para atender
            if fila != [] and esp == m[0]: #se houver gente para atender e a especialidade da fila coincidir com a do médico
                dequeue2(queueConsulta, m[0]) #remove um elemento da fila
                m[3] = True #médico passa a estar ocupado
    return f"Id: {m[1]} atendeu paciente"
# ---

# --- Utilização das distribuições para gerar chegadas e durações das consultas
# ---
def gera_intervalo_tempo_chegada(lmbda):   # é definido um intervalo random entre a chegada de cada paciente 
    return np.random.exponential(1 / lmbda) 


def gera_tempo_consulta(): #gera o tempo que a consulta vai demorar de acordo com a distribuição que foi definida
    if DISTRIBUICAO_TEMPO_CONSULTA == "exponential":
        return np.random.exponential(TEMPO_MEDIO_CONSULTA)
    elif DISTRIBUICAO_TEMPO_CONSULTA == "normal":
        return max(0, np.random.normal(TEMPO_MEDIO_CONSULTA, 5))
    elif DISTRIBUICAO_TEMPO_CONSULTA == "uniform":
        return np.random.uniform(TEMPO_MEDIO_CONSULTA * 0.5, TEMPO_MEDIO_CONSULTA * 1.5)

# --- Funções auxiliares
# -----------------------------------------
# --- Procura o primeiro médico livre
# ---
def procuraMedicoEsp(lista, esp): #procura um médico livre a partir da especialidade
    res = None
    i = 0
    encontrado = False #se encontrou ou não um médico livre
    while not encontrado and i < len(lista): 
        if lista[i][0] == esp and not lista[i][3]: # se a especialidade do médico coincide com a especialidade pretendida e se ele não estiver ocupado vamos fazer o resto
            res = lista[i] #descobri um médico livre
            encontrado = True #diz que encontrei um médico livre e por consequência nãp permite que o ciclo recomece
        i = i + 1
    return res #retorna o médico que está ocupado

# -----------------------------------------
#funções para o auxílio da parte relacionada com a estatística 

def maiortamanhoqueue(tamanhos): #esta função calcula o tamanho máximo de uma queue a partir de uma lista de tamanhos da queue
    max = 0
    for tamanho in tamanhos:
        if tamanho > max:
            max = tamanho
    return max

def tmedio(coisas): #calcula a média dos dados presentes numa lista
    if len(coisas) == 0:
        return 'Sem dados'
    else:
        soma = 0
        for coisa in coisas:
            soma = soma + coisa
        return soma / len(coisas)

def taxa_ocupacao_medicos(medicos): #calcula a taxa de ocupação dos médicos
    ocupados = 0
    for m in medicos:
        if m[3]:  # m[3] == ocupado; se o médico estiver ocupado vamos atualizar o valor de ocupados e no fim fazer o calculo da percentagem de médicos que estão ocupados
            ocupados += 1
    return ocupados / len(medicos)

def taxa_ocupacao_recepcionistas(recepcionistas): #faz a mesma coisa que a função de cima, mas é para as rececionistas
    ocupados = 0
    for r in recepcionistas:
        if r[3]:  # r[3] == ocupado
            ocupados += 1
    return ocupados / len(recepcionistas)

def percent(tempos, tsimula): #calcula uma percentagem 
    soma = 0
    for tempo in tempos:
        soma = soma + tempo
    return (soma/tsimula)*100

def tmedocup(lista, tsimula): # calcula a média do tempo que os proficionais estiveram ocupados
    listadeocupacoes = []
    for _,tempo in lista:
        listadeocupacoes.append((tempo/tsimula)*100) #coloca a percentagem do tempo que os proficionais estiveram ocupados
    soma = 0
    for percent in listadeocupacoes:
        soma = soma + percent #calcula a soma de todas as percentagens para que depois possa ser feita a média
    if len(listadeocupacoes) != 0:
        media = soma/len(listadeocupacoes) #calcula a média
        return media
    else:
        return 'Sem dados'

def atualiztamanhoqueue(dict, queue, e): #se tudo correr bem, esta função deverá ver em que especialidades é que o doente está e de acordo com essa especialidade adicionar o tamnho da queue na zona correta.
    if e_especialidade(e) == 'Pediatria':
        dict['tamanho_qp'].append(len(queue[4][1]))
    elif e_especialidade(e) == 'Clinica Geral':
        dict['tamanho_qcg'].append(len(queue[3][1]))
    elif e_especialidade(e) == 'Ortopedia':
        dict['tamanho_qo'].append(len(queue[1][1]))
    elif e_especialidade(e) == 'Cardiologia':
        dict['tamanho_qc'].append(len(queue[0][1]))
    elif e_especialidade(e) == 'Dermatologia':
        dict['tamanho_qd'].append(len(queue[2][1]))
    return dict

def atualiztamanhoqueuetempos(dict, queue, e, tempo): #se tudo correr bem, esta função deverá ver em que especialidades é que o doente está e de acordo com essa especialidade adicionar o tempo passado e o tamnho da queue na zona correta.
    if e_especialidade(e) == 'Pediatria':
        dict['tamanho_qp_tempos'].append((tempo, len(queue[4][1])))
    elif e_especialidade(e) == 'Clinica Geral':
        dict['tamanho_qcg_tempos'].append((tempo, len(queue[3][1])))
    elif e_especialidade(e) == 'Ortopedia':
        dict['tamanho_qo_tempos'].append((tempo, len(queue[1][1])))
    elif e_especialidade(e) == 'Cardiologia':
        dict['tamanho_qc_tempos'].append((tempo, len(queue[0][1])))
    elif e_especialidade(e) == 'Dermatologia':
        dict['tamanho_qd_tempos'].append((tempo, len(queue[2][1])))
    return dict

def atualiztespera(dict, tempo, e): #se tudo correr bem, esta função deverá fazer o mesmo que a função de cima, mas com os tempos de espera.
    if e_especialidade(e) == 'Pediatria':
        dict['espera_consulta_pediatria'].append(tempo-e_tempo(e))
    elif e_especialidade(e) == 'Clinica Geral':
        dict['espera_consulta_clinica_geral'].append(tempo-e_tempo(e))
    elif e_especialidade(e) == 'Ortopedia':
        dict['espera_consulta_ortopedia'].append(tempo-e_tempo(e))
    elif e_especialidade(e) == 'Cardiologia':
        dict['espera_consulta_cardiologia'].append(tempo-e_tempo(e))
    elif e_especialidade(e) == 'Dermatologia':
        dict['espera_consulta_dermatologia'].append(tempo-e_tempo(e))
    return dict

def atualiztconsult(dict, med, tconsulta): #atualiza o dicionário de forma a que ele passe a ter o tempo total que um médico esteve ocupado
    i = 0 
    encontrado = False 
    while i < len(dict['ocupacao_medicos']) and encontrado == False:
        if dict['ocupacao_medicos'][i][0] == m_id(med): #se encontrou o médico
            dict['ocupacao_medicos'][i][1] = dict['ocupacao_medicos'][i][1] + tconsulta #atualiza o tempo ´total que esse médico esteve ocupado
            encontrado = True #diz que encontrou o médico para que não seja preciso continuar a procurar
        i = i + 1
    if encontrado == False: #se não encontrou o médico cria uma nova lista com o tempo que o médico passou m«na consulta (foi o tempo que ele esteve ocupado)
        dict['ocupacao_medicos'].append([m_id(med), tconsulta])
    return dict

def atualiztatend(dict, recep, tatend): #faz a mesma coisa que o de cima, mas é para os rececionistas
    i = 0 
    encontrado = False
    while i < len(dict['ocupacao_recepcionistas']) and encontrado == False:
        if dict['ocupacao_recepcionistas'][i][0] == r_id(recep):
            dict['ocupacao_recepcionistas'][i][1] = dict['ocupacao_recepcionistas'][i][1] + tatend
            encontrado = True
        i = i + 1
    if encontrado == False:
        dict['ocupacao_recepcionistas'].append([r_id(recep), tatend])
    return dict

def tempclinic(dict, e, lista, tempo): #atualiza o dicionário que terá a lista dos tempos totais na clínica
    if e_id(e) in lista: #se o id do doente estiver na lista
        tempo_chegada = lista[e_id(e)] # diz quando é qeu o doente chegou a clinica
        dict['tempo_total_clinica'].append(tempo-tempo_chegada) #adiciona a lista de tempos totais na clinica o tempo que o doente esteve lá
    return dict

def tamanho_medio_fila_rececao(estatisticas): #calcula o tamanho médio da queue da receção
    fila = estatisticas["tamanho_queue_atendimento"]
    if len(fila) == 0:
        return 0
    return sum(fila) / len(fila) #divide o somatório de todos os tamanhos da fila de atendimento pelo total de tamanhos


# -----------------------------------------
# funções para a criação dos gráficos

def grafico_ocupacao_medicos(estatisticas): #cria o gráfico que mostra a evolução da taxa de ocupação dos médicos ao londo do tempo da simulação
    ajuste = sorted(estatisticas["ocupacao_medicos_tempo"], key=lambda x: x[0])
    if not ajuste:
        return

    tempos = [t for t, _ in ajuste] #cria a lista só com os tempos
    taxas = [v for _, v in ajuste] #cria a lista com as taxas de ocupação que, como as listas estão ordenadas, vão coincidir com os tempos que estão na mesma posição da lista de cima

    plt.figure(figsize=(10, 5))
    plt.step(tempos, taxas, where="post")
    plt.xlabel("Tempo (min)")
    plt.ylabel("Taxa de ocupação dos médicos")
    plt.title("Evolução da taxa de ocupação dos médicos")
    plt.ylim(0, 1)
    plt.grid(True)


def grafico_ocupacao_recepcionistas(estatisticas): #faz a mesma coisa que o de cima, mas é para as rececionistas
    ajuste2 = sorted(estatisticas["ocupacao_recepcionistas_tempo"], key=lambda x: x[0])
    if not ajuste2:
        return

    tempos = [t for t, _ in ajuste2]
    taxas = [v for _, v in ajuste2]

    plt.figure(figsize=(10, 5))
    plt.step(tempos, taxas, where="post")
    plt.xlabel("Tempo (min)")
    plt.ylabel("Taxa de ocupação das rececionistas")
    plt.title("Evolução da taxa de ocupação das rececionistas")
    plt.ylim(0, 1)
    plt.grid(True)


def grafico_filas(estatisticas): #gera o gráfico que mostra como variam as filas de espera ao longo do tempo
    plt.figure(figsize=(10, 6))
    grafs = [("Cardiologia","tamanho_qc_tempos"),("Ortopedia","tamanho_qo_tempos"),("Dermatologia","tamanho_qd_tempos"),("Clínica Geral","tamanho_qcg_tempos"),("Pediatria","tamanho_qp_tempos")] #nome da especialidade e nome da chave que contem os dados para a formação do gráfico dessa especialidade
    
    for esp, lista in grafs:
        ajuste3 = sorted(estatisticas[lista], key=lambda x: x[0]) #ordena a lista
        if ajuste3:
            tempos = [t for t, _ in ajuste3] #cria a lista dos tempos
            tamanhos = [v for _, v in ajuste3] #cria a lista dos tamanhos
            plt.step(tempos, tamanhos, where="post", label = esp)

    plt.xlabel("Tempo (min)")
    plt.ylabel("Tamanho da fila")
    plt.title("Filas de espera por especialidade")
    plt.legend()
    plt.grid(True)

#------------------------------------------------------------------------

def simula(dados):

    #dados fornecidos pelo utilizador

    RECEPCIONISTAS = dados['recep']
    TEMPO_SIMULACAO = dados['temp']*60
    MEDICOS = {
        'Cardiologia': dados['mcardio'],
        'Ortopedia': dados['morto'],
        'Dermatologia': dados['mderm'],
        'Clinica Geral': dados['mcg'],
        'Pediatria': dados['mpedi']
    }

    estatisticas = {
    "espera_rececao": [], #o tempo que esperou na fila de espera para ser atendido
    "espera_consulta_pediatria": [], #tempo que esperou para ser atendido em pediatria
    "espera_consulta_clinica_geral": [], #tempo que esperou para ser atendido em clinica geral
    "espera_consulta_ortopedia": [], #tempo que esperou para ser atendido em ortopedia
    "espera_consulta_dermatologia": [], #tempo que esperou para ser atendido em dermatologia
    "espera_consulta_cardiologia": [], #tempo que esperou para ser atendido em cardiologia
    "tempo_consulta": [], #quanto tempo demorou a consulta
    "tempo_atendimento": [], #quanto tempo demorou o atendimento
    "tamanho_queue_atendimento": [], #tamanho da queue ao longo do tempo (contabilizada sempre que há um novo doente na fila ou quando sai um doente da fila)
    "tamanho_qp": [], #mesma cena, mas para as especialidades
    "tamanho_qcg": [],
    "tamanho_qo": [],
    "tamanho_qd": [],
    "tamanho_qc": [],
    "tamanho_queue_atendimento_tempos": [], #constituido por tuplos que contêm o tamanho e quando é que a queue teve esse tamanho
    "tamanho_qp_tempos": [], #mesma coisa que o de cima
    "tamanho_qcg_tempos": [],
    "tamanho_qo_tempos": [],
    "tamanho_qd_tempos": [],
    "tamanho_qc_tempos": [],
    "tempo_total_clinica": [],
    "ocupacao_medicos": [], 
    "ocupacao_medicos_tempo": [], #key → id do médico ;value → lista de tempos de atendimento desse médico; cada nova consulta → append
    "ocupacao_recepcionistas": [], #key → id do rececionista ;value → lista de tempos de atendimento desse rececionista; cada novo atendimento → append
    "ocupacao_recepcionistas_tempo": []
}

    Events = []

    #Contagem de tempo começa em zero
    tempo_atual = 0.0
    
    # Nossa simulação leva em conta duas Queues. A primeira Queue, a da entrada, todos os pacientes
    # que chegam entram, e são organizados conforme características de prioridade
    # pessoas de mais de 65 anos são atendidas primeiro.
    # A segunda Queue depende da especialidade para entrar, e internamente é organizada
    # pela gravidade. 

    # Lista de recepcionistas e contador de Recepcionistas para gerar id
    recepcionistas = []
    contadorRecepcionistas = 1

    #adicionar recepcionistas a lista inicial de recionistas 
    for i in range(RECEPCIONISTAS): #RECEPCIONISTA retoma a variável número de recepcionistas selecionados na simulação
        recepcionistas.append(['r' + str(contadorRecepcionistas), False, None, 0.0, 0.0]) # para diferenciar os IDs de médicos e recepcionistas, mudamos o prefixo 
        contadorRecepcionistas += 1
        # as/os recepcionistas vão ter um modelo semelhante ao modelo dos médicos para podermos utilizar o mesmo método para as estatísticas.

    # Lista de médicos e contador de Médicos para gerar id 
    medicos = []
    contadorMedicos = 1

    #adicionar médicos a lista inicial de médicos
    for esp, num in MEDICOS.items(): 
        for i in range(num): # [esp: String, id: String, sala: String, ocupado: Boolean, doente_corrente: String, total_tempo_ocupado: Float, inicio_ultima_consulta: Float]
            medicos.append([esp,'d' + str(contadorMedicos), 's' + str(contadorMedicos), False, None, 0.0, 0.0])
            contadorMedicos += 1

    # As Queues 
    queueEventos = [] # Lista de eventos que vão acontecer, ordenada por tempo de ocorrência do evento
    queueAtendimento = [] # Fila de espera - doentes à espera de serem atendidos na receção
    queueConsulta = [["Cardiologia", []], ["Ortopedia", []], ["Dermatologia", []], ["Clinica Geral", []] ,["Pediatria", []]]
    
    # --- Geração das chegadas de doentes

    # Contador de doente para gerar ID de paciente
    contadorDoentes = 1

    chegadas = {} # dicionário de suporte para a geração das consultas

    tempos = gera_tempos_chegada()

    for tchegada in tempos:
        if tchegada > TEMPO_SIMULACAO: # isto serve para evitar que caso seja gerado um tempo que seja maior do que a simulação o ciclo continue
            break
        else:
            doente_id = "p" + str(contadorDoentes) # uso do prefixo 'p' para paciente
            chegadas[doente_id] = tchegada
            ev = gravidade_doente(especialidade_doente(pacientes_tchegadas([tchegada], 'pessoas.json')))
            evento = ev[0] #temos que fazer isto porque nós fizemos a função para devolver uma lista de eventos, mas ao fazer a chamada dos tempos 1 a 1 vamos criar uma lista com apenas 1 evento lá dentro ou seja uma lista dentro de uma lista
            queueEventos = enqueue(queueEventos, [tchegada, CHEGADA, doente_id, e_doente(evento), e_idade(evento), e_especialidade(evento), e_gravidade(evento)])
            contadorDoentes += 1
    
    # --- Tratamento dos eventos
    doentes_atendidos = 0 #número de doentes atendidos 

    while queueEventos != []: #vamos começara a atender os doentes e retirar aos poucos da queueEventos 
        evento, queueEventos = dequeue(queueEventos)  # para cada envento na queueEventos, vamos fazer o dequeue
        print(e_tipo(evento), evento) # vamos fazer o print do tipo de evento e o evento
        tempo_atual = e_tempo(evento) # o tempo atual é o tempo do evento

        if e_tipo(evento) == CHEGADA: # se o tipo de evento for chegada
            rececionista_livre = procuraRececionista(recepcionistas) #vamos ver se há rececionistas livres 
            if rececionista_livre:
                estatisticas['espera_rececao'].append(0) #tem que ser 0 porque ele não esperou nada 
                rececionista_livre = rOcupa(rececionista_livre) # a rececionista ficou ocupada
                estatisticas["ocupacao_recepcionistas_tempo"].append((tempo_atual, taxa_ocupacao_recepcionistas(recepcionistas))) #atualiza as estatísticas
                rececionista_livre = rInicioRececao(rececionista_livre, tempo_atual) 
                tempo_atendimento = gera_tempo_atendimento() 
                atualiztatend(estatisticas, rececionista_livre, tempo_atendimento) #para atualizar as estatísticas
                estatisticas['tempo_atendimento'].append(tempo_atendimento) 
                rececionista_livre = rDoenteCorrente(rececionista_livre, e_doente(evento)) # rececionista fica a atender o doente que acabou de chegar
                queueEventos = enqueue(queueEventos, [tempo_atual + tempo_atendimento, FIM_ATENDIMENTO, e_id(evento), e_doente(evento), e_idade(evento), e_especialidade(evento), e_gravidade(evento)]) #coloca na queue de eventos o novo evento em que o doente já foi atendido na receção
            else:
                queueAtendimento.append(evento) # doente fica à espera
                estatisticas['tamanho_queue_atendimento'].append(len(queueAtendimento)) #atualização das estatísticas
                estatisticas['tamanho_queue_atendimento_tempos'].append((tempo_atual,len(queueAtendimento)))
                print(f"Fila de Espera({len(queueAtendimento)}): ", queueAtendimento)

        elif e_tipo(evento) == FIM_ATENDIMENTO: #quando o doente já foi atendido na receção
            i = 0
            encontrado = False
            while i < len(recepcionistas) and not encontrado: # vou procurar a rececionista que está a atender o doente cujo atendimento terminou
                if r_doente_corrente(recepcionistas[i]) == e_doente(evento): # se encontrei a rececionista que está a atender o doente deste evento
                    recepcionistas[i] = rOcupa(recepcionistas[i]) # a rececionista ficou livre
                    recepcionistas[i] = rDoenteCorrente(recepcionistas[i], None)  # não está a atender nenhum doente
                    recepcionistas[i] = rTempoOcupado(recepcionistas[i], r_total_tempo_ocupado(recepcionistas[i]) + tempo_atual - r_inicio_ultima_rececao(recepcionistas[i])) # incremento o tempo do atendimento que terminou
                    encontrado = True
                i = i + 1

            rececionista = recepcionistas[i-1]

            if queueAtendimento != []: # se há doentes à espera vou ocupar a rececionista que ficou livre...
                ev, queueAtendimento = dequeue(queueAtendimento) #prox_doente, tchegada = ev
                tempo_chegada = e_tempo(ev)
                estatisticas['espera_rececao'].append(tempo_atual-tempo_chegada) #subtração do tempo de chegada ao tempo atual para saber quanto tempo é que o doente ficou efetivamente a espera. Se colocar apenas o tempo atual a espera não correspoderia ao tempo que o doente esperou desde que chegou a clinica, mas sim a soma do tempo que ele esperou + o tempo de simulação até a chegada do doente.
                estatisticas['tamanho_queue_atendimento'].append(len(queueAtendimento))
                estatisticas['tamanho_queue_atendimento_tempos'].append((tempo_atual, len(queueAtendimento)))
                rececionista = rOcupa(rececionista)
                rececionista = rInicioRececao(rececionista, tempo_atual)
                rececionista = rDoenteCorrente(rececionista, e_doente(ev))
                tempo_atendimento = gera_tempo_atendimento()
                atualiztatend(estatisticas, rececionista, tempo_atendimento) #isto foi alterado
                estatisticas['tempo_atendimento'].append(tempo_atendimento)
                queueEventos = enqueue(queueEventos, [tempo_atual + tempo_atendimento, FIM_ATENDIMENTO, e_id(ev), e_doente(ev), e_idade(ev), e_especialidade(ev), e_gravidade(ev)])
            
            medico_livre = procuraMedicoEsp(medicos, e_especialidade(evento))
            if medico_livre:
                tempo_chegada = e_tempo(evento)
                atualiztespera(estatisticas, tempo_chegada, evento) #isto deverá dar 0 se tudo estiver a funcionar como eu gostaria  porque o doente não esperou.
                medico_livre = mOcupa(medico_livre) # o medico ficou ocupado
                estatisticas["ocupacao_medicos_tempo"].append((tempo_atual, taxa_ocupacao_medicos(medicos)))
                medico_livre = mInicioConsulta(medico_livre, tempo_atual)
                tempo_consulta = gera_tempo_consulta()
                atualiztconsult(estatisticas, medico_livre, tempo_consulta) #isto foi alterado por questões de coesão
                medico_livre = mDoenteCorrente(medico_livre, e_doente(evento)) # medico fica a atender o doente que acabou de chegar
                queueEventos = enqueue(queueEventos, [tempo_atual + tempo_consulta, SAIDA, e_id(evento), e_doente(evento), e_idade(evento), e_especialidade(evento), e_gravidade(evento)])
            else:
                queueConsulta = enqueue2(evento, queueConsulta) # doente fica à espera 
                atualiztamanhoqueue(estatisticas, queueConsulta, evento) #estou a tentar que seja atualizada a lista dos tamanhos das filas de espera de acordo com a especilidade do doente que colocado na queue.
                atualiztamanhoqueuetempos(estatisticas, queueConsulta, evento, tempo_atual) #está a fazer o mesmo que em cima, mas com os tempos
                print(f"Filas de Espera({len(queueConsulta)}): ", queueConsulta)

        elif evento[1] == SAIDA: # Vamos libertar o médico e despachar o doente
            doentes_atendidos += 1
            i = 0
            encontrado = False 
            while i < len(medicos) and not encontrado: # vou procurar o médico que está a atender o doente cuja consulta terminou
                if m_doente_corrente(medicos[i]) == e_doente(evento): # se encontrei o médico que está a atender o doente deste evento
                    medicos[i] = mOcupa(medicos[i]) # o médico ficou livre
                    estatisticas["ocupacao_medicos_tempo"].append((tempo_atual, taxa_ocupacao_medicos(medicos)))
                    tempclinic(estatisticas, evento, chegadas, tempo_atual)
                    medicos[i] = mDoenteCorrente(medicos[i], None)  # não está a atender nenhum doente
                    medicos[i] = mTempoOcupado(medicos[i], m_total_tempo_ocupado(medicos[i]) + tempo_atual - m_inicio_ultima_consulta(medicos[i])) # incremento o tempo da consulta que terminou
                    medicoc = medicos[i] #só para não causar problemas com os indices
                    encontrado = True
                i = i + 1

            #medico = medicos[i-1]

            if encontrado: # se há doentes à espera vou ocupar o médico que ficou livre...
                ev, queueConsulta = dequeue2(queueConsulta, medicoc[0]) #prox_doente, tchegada = ev
                if ev is not None:
                    atualiztespera(estatisticas, tempo_atual, ev) 
                    atualiztamanhoqueue(estatisticas, queueConsulta, ev) #estou a tentar fazer o mesmo que fiz em cima
                    atualiztamanhoqueuetempos(estatisticas, queueConsulta, ev, tempo_atual)
                    medicoc = mOcupa(medicoc)
                    medicoc = mInicioConsulta(medicoc, tempo_atual)
                    medicoc = mDoenteCorrente(medicoc, e_doente(ev))
                    tempo_consulta = gera_tempo_consulta()
                    atualiztconsult(estatisticas, medicoc, tempo_consulta) #acrescentado
                    queueEventos = enqueue(queueEventos, [tempo_atual + tempo_consulta, SAIDA, e_id(ev), e_doente(ev), e_idade(ev), e_especialidade(ev), e_gravidade(ev)])
                    
    print(f"Doentes atendidos: {doentes_atendidos}") 
    print(f""" Tempo médio de espera na receção: {tmedio(estatisticas['espera_rececao'])}
               Tempo médio de atendimento na receção: {tmedio(estatisticas['tempo_atendimento'])} 
               Tempos médios de espera para consulta: Cardiologia: {tmedio(estatisticas['espera_consulta_cardiologia'])} 
                                                      Ortopedia: {tmedio(estatisticas['espera_consulta_ortopedia'])}
                                                      Dermatologia: {tmedio(estatisticas['espera_consulta_dermatologia'])}
                                                      Clinica geral: {tmedio(estatisticas['espera_consulta_clinica_geral'])}
                                                      Pediatria: {tmedio(estatisticas['espera_consulta_pediatria'])}
               Tempo médio na clínica: {tmedio(estatisticas['tempo_total_clinica'])}
               Tamanhos máximos das queues: Queue de atendimento: {maiortamanhoqueue(estatisticas['tamanho_queue_atendimento'])}
                                            Queue de cardiologia: {maiortamanhoqueue(estatisticas['tamanho_qc'])}
                                            Queue de ortopedia: {maiortamanhoqueue(estatisticas['tamanho_qo'])}
                                            Queue de dermatologia: {maiortamanhoqueue(estatisticas['tamanho_qd'])}
                                            Queue de clinica geral: {maiortamanhoqueue(estatisticas['tamanho_qcg'])}
                                            Queue de pediatria: {maiortamanhoqueue(estatisticas['tamanho_qp'])}
               Tamanhos médios das queues:  Queue de atendimento: {tmedio(estatisticas['tamanho_queue_atendimento'])}
                                            Queue de cardiologia: {tmedio(estatisticas['tamanho_qc'])}
                                            Queue de ortopedia: {tmedio(estatisticas['tamanho_qo'])}
                                            Queue de dermatologia: {tmedio(estatisticas['tamanho_qd'])}
                                            Queue de clinica geral: {tmedio(estatisticas['tamanho_qcg'])}
                                            Queue de pediatria: {tmedio(estatisticas['tamanho_qp'])}
               Ocupação média dos médicos: {tmedocup(estatisticas['ocupacao_medicos'], TEMPO_SIMULACAO)}
               Ocupação média das recepcionistas: {tmedocup(estatisticas['ocupacao_recepcionistas'], TEMPO_SIMULACAO)}""")
    
    grafico_ocupacao_medicos(estatisticas) #gera o gráfico da ocupação dos médicos
    grafico_ocupacao_recepcionistas(estatisticas) #gera o gráfico da ocupação dos rececionistas
    grafico_filas(estatisticas) #gera o gráfico com os tamanhos das queues

    plt.show() 