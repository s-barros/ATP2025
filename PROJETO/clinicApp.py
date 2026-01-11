import FreeSimpleGUI as sg
import faux_clinic as fc
import clinic_registo as cr
import clinic_login as cl
import simula_graf_test_final as sim
import clinic_dados_simulacao as cd
import json

if __name__ == "__main__":
    users = fc.carregaBD("clinic_users.json") #carrega a base de dados com os utilizadores registados 
    user = cl.login(users) #atribui o nome de user ao utilizador que foi autenticado 
    historico = fc.carregaBD("clinic_historico.json") # carrega a base de dados que tem todos os históricos dos utilizadores

    sg.theme("DarkBrown")
    layout_data_area = [ #faz com que apareça na lateral da janela olá e o nome do utilizador autenticado
        [sg.Text(f"Olá {user['nome']}")]
    ]

    layout_menu = [ #estrutura da janela
        [sg.Text("Simulação da Clínica", font=('Arial', 36))],
        [sg.Button("Simular", key='-SIMULA-', font=('Arial', 24)),
        sg.Button("Histórico", key='-HIST-', font=('Arial', 24))],
        [sg.HSep(color='white')],
        [sg.Text(key='-LOG-')]
    ]

    layout_principal = [ #estrutura da coluna lateral da janela onde aparece o Olá utilizador
        [sg.Column(layout_menu), sg.VSep(color='white'), sg.Column(layout_data_area)]
    ]

    if user: # - Se o login tiver sucesso, a interface principal é lançada
        wprincipal = sg.Window("Clinic Menu Principal", layout_principal, location=(50,50))
        stop = False
        while not stop:
            event, values = wprincipal.read() #fazer a leitura do que está a acontecer na janela

            if event == sg.WIN_CLOSED: #fecha a janela
                stop = True

            elif event == '-SIMULA-': #o que acontece se o utilizador selecionar a opção de simular
                dados_user = cd.janela() #variável que contém os dados que foram recolhidos depois da abertura e da colocação dos dados nos campos da janela de recolha que abriu no momento em que o utilizador carregou em simular
                if dados_user: #verifica se temos dados para simular. se sim: = True simulação corre, caso contrário não corre nada e não dá erro por não haver dados.
                    sim.simula(dados_user) #faz a simulação com os dados fornecidos pelo utilizador
                    fc.aidicionahist(historico,user["nome"], dados_user) #adiciona os dados ao historico do utilizador
                    fc.gravaBD("clinic_historico.json",historico) #garava o historico de forma a evitar perdas de dados caso o programa vá a baixo por alugma razão

            elif event == '-HIST-': # se o utilizador optar por ver o seu histórico 
                hist_user = fc.listahist(historico, user["nome"])
                if hist_user is None: # se não encontrar o utilizador no histórico
                    sg.popup("Utilizador sem histórico.")
                elif len(hist_user) == 0: #se o utilizador ainda não tiver feito nenhuma simulação aparece um pop up a dizer que não tem nenhum histórico 
                    sg.popup("Ainda não existem simulações guardadas.")
                else: # se encontrar o utilizador e ele tiver coisas no histórico vamos estar a mostrar um pop up com todas os dados das simulações que ele já fez
                    texto = ""
                    for i, h in enumerate(hist_user, start=1):
                        texto += f"Simulação {i}\n{json.dumps(h, indent=2, ensure_ascii=False)}\n\n" #cria o texto que será mostrado no pop up. Qual é que foi a simulação que ele fez e que dados foram recolhidos.
                    
                    sg.popup_scrolled( #cria a janela de forma a que se possa navegar para cima a para baixo caso o texto não caiba todo na janela
                        texto,
                        title="Histórico de Simulações",
                        size=(80, 30)
                    )
                

    wprincipal.close() #fecha a janela

    # - Gravar tudo antes de sair
    fc.gravaBD("clinic_users.json", users)  
    fc.gravaBD("clinic_historico.json", historico)