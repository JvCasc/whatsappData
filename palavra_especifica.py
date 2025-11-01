import pandas as pd

thigela = pd.read_csv("thigela.csv")

thigela["Mensagem"] = thigela["Mensagem"].astype(str)

def conta_ocorrencias(nome_pessoa, palavra, tabela):
    mensagem_pessoa = tabela[tabela["Nome"] == nome_pessoa]["Mensagem"]

    contagem_palavras = mensagem_pessoa.apply(lambda x: x.lower().split().count(palavra.lower())).sum()

    return contagem_palavras

# Defina o nome da pessoa e a palavra a ser pesquisada
nome_pessoa = "Gouvea"  # Substitua pelo nome da pessoa
palavra = "comida"  # Substitua pela palavra que deseja contar

# Chamar a função para contar as ocorrências
contagem = conta_ocorrencias(nome_pessoa, palavra, thigela)

# Exibir o resultado
print(f'A palavra "{palavra}" foi usada {contagem} vezes por {nome_pessoa}.')

