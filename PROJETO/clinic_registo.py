# ---
# - Login na aplicação clinicApp
# - 2025-11-27 by grupo 28
# -------------------------------
import FreeSimpleGUI as sg
import faux_clinic as fc

users = fc.carregaBD('clinic_users.json')

def registar():
    sg.theme("DarkBrown")
    layout = [ #estrutura da janela
        [sg.Text("Nome:"), sg.InputText(key='-NOME-')],
        [sg.Text("Password:"), sg.InputText(key='-PASS-')],
        [sg.Text("Id:"), sg.InputText(key='-ID-')],
        [sg.Button("Confirmar", key='-CONFIRMAR-'), sg.Button("Cancelar", key='-CANCELAR-')],
        [sg.HSep(color='white', pad=(30,30))],
        [sg.Text(key='-LOG-')]
    ]

    # Criar a janela
    wreg = sg.Window("TarefasApp: Janela de Registo", layout, location=(200,100), font=('Arial', 24))

    stop = False
    user = None
    while not stop:
        event, values = wreg.read() #ler o que está a acontecer na janela

        if event in ["-CANCELAR-", sg.WIN_CLOSED]: #fecha a janela caso o utilizador decida cancelar
            stop = True
        elif event == '-CONFIRMAR-': #se o utilizador preencher os campos e selecionar confirmar os dados serão adicionados a lista de users do ficheiro clinic_users
            user = { #cria o dicionário com os dados inseridos pelo utiliador, que será adicionado a lista
                'id': values['-ID-'],
                'nome': values['-NOME-'],
                'password': values['-PASS-']
            }
            users.append(user) #adiciona o dicionário a lista
            fc.gravaBD("clinic_users.json", users) #garava o ficheiro 
            sg.popup("Utilizador registado com sucesso!") #cria um pop up a dizer que o utilizador foi registado com sucesso
            stop = True
        else:
            print(event, ": ", values)

    wreg.close() #fecha a janela
