# API https://viacep.com.br/
import requests

# Deve se passar uma CEP de 8 digitos sem pontuação para API

def pesquisa_CEP(cep_digitado):
    cep = cep_digitado.replace('.', '').replace('-', '')

    if len(cep) != 8:
        return 'CEP inválido ou não localizado'
    
    # Chamado da API ViaCEP em formato JSON - endpoint
    link = f'https://viacep.com.br/ws/{cep}/json/'

    # Requisição dos dados da API (API retorna 200 caso de certo e 400 em caso de erro)
    
    requisicao = requests.get(link)

    # A função json() traduz os dados JSON da API e retorna um dicionário com todos os dados do CEP
    dic_requisicao = requisicao.json()
    # Retorna os dados do CEP em formato de dicionário
    # print(requisicao.json())

    # Dados extraídos do dicionário
    try:
        cidade_uf = f"{dic_requisicao['localidade']} - {dic_requisicao['uf']}"
        rua = dic_requisicao['logradouro']
        bairro = dic_requisicao['bairro']
    except KeyError:
        return 'CEP inválido ou não localizado'

    return f"{rua}, {bairro}, {cidade_uf}"

