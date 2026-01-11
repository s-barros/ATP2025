#código para a janela que aparece quando o utilizador seleciona simular
#esta janela permite que o utilizador possa escolher quantos médicos, rececionistas, etc.. é que a simulação vai usar.

import FreeSimpleGUI as sg
import faux_clinic as fc


def janela():
    sg.theme("DarkBrown")
    layout = [ #estrutura da janela (botões, texto, etc...)
        [sg.Text("Por favor coloque sempre números maiores do que 0", font=('Arial', 36))],
        [sg.Text("Número de recepcionistas:"), sg.InputText(default_text = "1", key='-RECEP-')],
        [sg.Text("Número de médicos de cardiologia:"), sg.InputText(default_text = "1", key='-MCARDIO-')],
        [sg.Text("Número de médicos de ortopedia:"), sg.InputText(default_text = "1", key='-MORTO-')],
        [sg.Text("Número de médicos de dermatologia:"), sg.InputText(default_text = "1", key='-MDERM-')],
        [sg.Text("Número de médicos de clínica geral:"), sg.InputText(default_text = "1", key='-MCG-')],
        [sg.Text("Número de médicos de pediatria:"), sg.InputText(default_text = "1", key='-MPEDI-')],
        [sg.Text("Tempo de simulação (horas):"), sg.InputText(default_text = "1", key='-TSIM-')],
        [sg.Button("Confirmar", key='-CONFIRMAR-'), sg.Button("Cancelar", key='-CANCELAR-')]
    ]

    # Criar a janela
    wreg = sg.Window("ClinicApp: Janela de Dados para a simulação", layout, location=(150,100), font=('Arial', 24))

    stop = False
    dados = None
    while not stop:
        event, values = wreg.read() # vamos estar a ler aquilo que a janela está a receber

        if event in ["-CANCELAR-", sg.WIN_CLOSED]: #fecha a janela quando o utilizador seleciona cancelar
            stop = True
        elif event == '-CONFIRMAR-': # recolhe os dados para os passar para a simulação
            dados = {
                'mcardio': int(values['-MCARDIO-']),
                'morto': int(values['-MORTO-']),
                'mderm': int(values['-MDERM-']),
                'mcg': int(values['-MCG-']),
                'mpedi': int(values['-MPEDI-']),
                'recep': int(values['-RECEP-']),
                'temp': int(values['-TSIM-']),
            }
            
            stop = True
        else:
            print(event, ": ", values)

    wreg.close() #fecha a janela
    return dados #faz o return dos dados para poderem ser usados na simulação