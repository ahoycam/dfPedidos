import pandas as pd

planilha = 'DEZEMBRO 2023.xlsx'
df = pd.read_excel(planilha)

datas, nomes, itens, valores, quantidades, totais = [], [], [], [], [], []  

for indice, linha in df.iterrows():
    data = linha['Data']
    nome = linha['Nome']
    item = linha['Itens']
    valor = linha['Valor']
    quantidade = linha['Quantidade']
    total = linha['Total']
    if not pd.isnull(data):
        datas.append(data)
        nomes.append(nome)
        itens.append(item)
        valores.append(valor)
        quantidade.append(quantidades)
        totais.append(total)

dados = pd.DataFrame({ 
    'Data': datas,
    'Nome': nomes,
    'Itens': itens,
    'Valore': valores,
    'Quantidade': quantidades,
    'Total': totais
})

print(dados.head())
