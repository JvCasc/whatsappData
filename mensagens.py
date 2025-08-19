import pandas as pd

thigela = pd.read_csv("thigela.csv") # Comando padrão para ler o .csv

contagem = thigela["Nome"].value_counts().reset_index() # Conta a quantidade de mensagens e da um reset_index 

contagem.columns = ["Nome", "Mensagens"] # Renomeia as colunas 

campeao = contagem.iloc[0] # Extrai somente a primeira linha 

print(f"Tabela de participantes do grupo: \n{thigela["Nome"].value_counts()}")

print(f"{campeao["Nome"]} foi quem mais enviou mensagens: {campeao["Mensagens"]} 👑")