import PySimpleGUI as sg
import pesquisa_endereco as pq_end
import pesquisa_cep as pq_cep

# Criando as janelas
def janela_principal():
    sg.theme('Reddit')
    layout = [
        [sg.Text('Selecione uma opção', expand_x=True, justification='c')],
        [sg.Push(), sg.Button('Localiza CEP'), sg.Push(), sg.Button('Localiza Endereço'), sg.Push()]
    ]
    return sg.Window('Localiza CEP/Endereço', layout, finalize=True)

def janela_localiza_endereco():
    sg.theme('Reddit')
    layout = [
        [sg.Text('Localizador de endereço pelo CEP', expand_x=True, justification='c')],
        [sg.Text('Digite o CEP'), sg.Input(key='CEP_informado')],
        [sg.Text(key='resposta')],
        [sg.Push(), sg.Button('Voltar'), sg.Button('Ok'), sg.Button('Cancelar'), sg.Push()],
    ]
    return sg.Window('Localiza endereço', layout, finalize=True)

def janela_localiza_CEP():
    sg.theme('Reddit')
    layout = [
        [sg.Text('Localizador de CEP pelo endereco', expand_x=True, justification='c')],
        [sg.Text('Digite a sigla do estado'), sg.Push(), sg.Input(key='uf_digitada')],
        [sg.Text('Digite a cidade'), sg.Push(), sg.Input(key='cidade_digitada')],
        [sg.Text('Digite a rua'), sg.Push(), sg.Input(key='rua_digitada')],
        [sg.Listbox(['Vazio'], key='resposta', s=(100,3))],
        [sg.Push(), sg.Button('Voltar'), sg.Button('Ok'), sg.Button('Cancelar'), sg.Push()],
    ]
    return sg.Window('Localiza CEP', layout, finalize=True)

# Atribuição das janelas
janela1, janela2, janela3 = janela_principal(), None, None

# Execução da interface
while True:
    # Leitura de todas as janelas, eventos e valores
    janela, evento, valor = sg.read_all_windows()
    # Encerrando programa ao clicar no X ou no botão cancelar
    if evento == sg.WIN_CLOSED or evento == 'Cancelar':
        break
    # Acessando janela de localização de endereço
    if janela == janela1 and evento == 'Localiza Endereço':
        janela2 = janela_localiza_endereco()
        janela1.hide()
    if janela == janela2 and evento == 'Voltar':
        janela2.hide()
        janela1.un_hide()
    if janela == janela2 and evento == 'Ok':
        janela['resposta'].update(pq_end.pesquisa_CEP(valor['CEP_informado']))
    # Acessando janela de localização de CEP
    if janela == janela1 and evento == 'Localiza CEP':
        janela3 = janela_localiza_CEP()
        janela1.hide()
    if janela == janela3 and evento == 'Voltar':
        janela3.hide()
        janela1.un_hide()
    if janela == janela3 and evento == 'Ok':
        janela['resposta'].update(pq_cep.pesquisa_endereco(valor['uf_digitada'].upper(), valor['cidade_digitada'], valor['rua_digitada']))

# Encerrando o programa
janela.close()