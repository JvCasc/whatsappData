import pandas as pd

thigela = pd.read_csv("thigela.csv")

pessoas = thigela["Nome"].drop_duplicates().to_list()

i = 0
j = 0;

mais_mensagem = 0;
nome_mais_mensagem = ""

for nome in pessoas:
    for index, row in thigela[thigela["Nome"] == nome].iterrows():
        i += 1
        if i > mais_mensagem:
            mais_mensagem = i
            nome_mais_mensagem = nome
    if "+55" not in nome:
        print(f"{nome} enviou {i} mensagens")
    i = 0

print("----------")
print(f"Quem enviou mais mensagem: {nome_mais_mensagem} com {mais_mensagem} mensagens 👑")