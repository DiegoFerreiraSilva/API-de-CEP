# API https://viacep.com.br/
import requests
from pprint import pprint # Biblioteca para um print mais "bonito"
import pandas as pd # Biblioteca para criação de tabelas

# Deve se passar uma Rua e Bairo de no minímo 3 caracteres para API
# A função json() traduz os dados JSON da API e retorna um dicionário com todos os dados do CEP
# Requisição dos dados da API (API retorna 200 caso de certo e 400 em caso de erro)

def pesquisa_endereco(uf, cidade, rua):

    if len(uf) != 2:
        return 'Digite uma sigla de estado válida'

    link = f'https://viacep.com.br/ws/{uf}/{cidade}/{rua}/json/'

    requisicao = requests.get(link)

    try:
        dic_requisicao = requisicao.json()
    except:
        return ['Endereço não localizado ou incorreto']
    
    # tabela = pd.DataFrame(dic_requisicao)
    enderecos = list()
    for dicionario in dic_requisicao:
        lista = list()
        lista.append(dicionario['cep'])
        lista.append(dicionario['logradouro'])
        lista.append(dicionario['bairro'])
        lista.append(dicionario['localidade'])
        lista.append(dicionario['uf'])
        lista.append(dicionario['complemento'])
        enderecos.append(lista)
    return enderecos

