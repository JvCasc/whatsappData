import pandas as pd

thigela = pd.read_csv("thigela.csv")

apagadas = thigela[thigela["Mensagem"] == "Mensagem apagada"]

pessoas = thigela["Nome"].drop_duplicates().to_list() # Pega os membros do grupo removendo duplicatas e colocando em uma lista

mais_mensagem = 0

nome_mais_mensagem = 0

i = 0
j = 0;

for nome in pessoas:
    for index, row in apagadas[apagadas["Nome"] == nome].iterrows():
        i += 1
        if i > mais_mensagem:
            mais_mensagem = i
            nome_mais_mensagem = nome
    if "+55" not in nome:
        if "Meta" not in nome:
            print(f"{nome} apagou {i} mensagens")
    i = 0

print("----------")
print(f"Quem apagou mais mensagem foi {nome_mais_mensagem} com {mais_mensagem} mensagens apagadas 👑")


