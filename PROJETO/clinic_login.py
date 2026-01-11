# ---
# - Login na aplicação tarefasApp
# - 2025-11-27 by grupo 28
# -------------------------------
import FreeSimpleGUI as sg
import faux_clinic as fc
import clinic_registo as cr

def login(clinic_users):
    sg.theme("DarkBrown")
    layout = [ # conteúdo da janela
        [sg.Text("username:"), sg.InputText(key='-USER-')],
        [sg.Text("password:"), sg.InputText(key='-PASS-')],
        [sg.Button("Ok", key='-OK-'), sg.Button("Cancelar", key='-CANCELAR-')], 
        [sg.Button("Registe-se", key='-REG-')],
        [sg.HSep(color='white', pad=(30,30))],
        [sg.Text(key='-LOG-')]
    ]

    # Criar a janela
    window = sg.Window("Clinic: Janela de Login", layout, location=(200,100), font=('Times New Roman', 24))

    stop = False
    user = None
    while not stop:
        event, values = window.read() # ler o que o utilizador está a fazer na janela

        if event in ["-CANCELAR-", sg.WIN_CLOSED]: #fechar a janela se o utiliador selecionar cancelar
            stop = True
        elif event == '-OK-':
            bd = fc.carregaBD("clinic_users.json") #carregar a base de dados que contém todos os utilizadores registados
            user = fc.verificaUser(bd, values['-USER-'], values['-PASS-']) # verificar se aquilo que o utilizador inseriu nos campos são válidas (se estão no ficheiro)
            if user: # se as credenciais forem válidas a janela vai fechar e será feito um print no terminal de quem é que entrou na aplicação
                print('Utilizador autenticado: ', user)
                stop = True
            else: # se as credenciais não forem válidas aparecerá na janela que as credenciais não são válidas e volta a por o campos vazios
                window['-LOG-'].update("Credenciais inválidas! Tente novamente...")
                window['-USER-'].update("")
                window['-PASS-'].update("")
        elif event == '-REG-': # se o utilizador optar por se registar (carregando no botão) aparecerá a janela de registo onde o utilizador irá colocar as suas credenciais e no fim quando o novo utilizador for registado a janela de registo fecha-se e aparece na janela de login que um novo utilizador foi registado
            user = cr.registar()
            window['-LOG-'].update(f"Novo utilizador registado com sucesso")
        else:
            print(event, ": ", values)
    window.close() # fecha a janela
    return user 
