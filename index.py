import pandas as pd 

def replicDataCell(df, coluna):
    df[coluna] = df[coluna].fillna(method='ffill')

    return df


planilha = 'DEZEMBRO 2023.xlsx'
df = pd.read_excel(planilha, 'Semana 1')

df = replicDataCell(df, 'DATA')
df = replicDataCell(df, 'CLIENTE')
df = replicDataCell(df, 'HORA')
df = replicDataCell(df, 'PAGAMENTO')

df = df[df['ITEM'] != 'NADA']

ultimoItem = df['ITEM'].last_valid_index()

if ultimoItem is not None:
    df = df.loc[:ultimoItem]

print(df.tail(60))

