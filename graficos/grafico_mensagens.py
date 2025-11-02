import pandas as pd
import matplotlib.pyplot as plt

thigela = pd.read_csv("thigela.csv") # Importação do dataset

pessoas = thigela["Nome"].drop_duplicates().to_list() # Pega os membros do grupo removendo duplicatas e colocando em uma lista

i = 0
j = 0;

qtd_mensagens = []
mais_mensagem = 0; 
nome_mais_mensagem = ""

for nome in pessoas:
    for index, row in thigela[thigela["Nome"] == nome].iterrows():
        i += 1
    qtd_mensagens.append(i)
    i = 0

mensagem_pessoa = pd.DataFrame({"nome": pessoas, "qtd_mensagem": qtd_mensagens})

mensagem_pessoa.plot.bar(x = "nome", y = "qtd_mensagem")

plt.show()