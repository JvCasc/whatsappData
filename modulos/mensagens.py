import pandas as pd

def falador(csv):
    thigela = pd.read_csv(csv) # Importação do dataset

    pessoas = thigela["Nome"].drop_duplicates().to_list() # Pega os membros do grupo removendo duplicatas e colocando em uma lista

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
        #if "+55" not in nome:
            #if "Meta" not in nome:
                #print(f"{nome} enviou {i} mensagens")
        i = 0

    return nome_mais_mensagem, mais_mensagem
    #print("----------")
    #print(f"Quem enviou mais mensagem: {nome_mais_mensagem} com {mais_mensagem} mensagens 👑")