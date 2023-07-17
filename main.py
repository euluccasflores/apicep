import requests
CEP = input("informe seu CEP")
print(len(CEP))
if len(CEP) == 8:
    link = f'https://viacep.com.br/ws/{CEP}/json/'
    requisicao = requests.get(link)
    dic_requisicao = requisicao.json()
    uf = dic_requisicao['uf']
    cidade = dic_requisicao['localidade']
    bairro = dic_requisicao['bairro']
    cep = dic_requisicao['cep']
    rua = dic_requisicao['logradouro']
    print(dic_requisicao)
    if rua == '':
        print('Genérico')
    if bairro == '':
        print('Genérico')
