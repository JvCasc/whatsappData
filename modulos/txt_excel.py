import pandas as pd
import re

def txt_to_csv(txt):

    # Inicializar listas para armazenar data, hora, nome e mensagens
    data_list = []
    hora_list = []
    nome_list = []
    mensagem_list = []

    # Regex para capturar as partes da mensagem
    pattern = r'(\d{2}/\d{2}/\d{4})\s(\d{2}:\d{2})\s-\s(.*?):\s(.*)'

    # Processar cada linha da conversa
    for line in txt:
        match = re.match(pattern, line)
        if match:
            # Capturando os grupos da regex
            data_list.append(match.group(1))  # Data
            hora_list.append(match.group(2))  # Hora
            nome_list.append(match.group(3))  # Nome
            mensagem_list.append(match.group(4))  # Mensagem
        else:
            # Se não corresponder, exibir linha problemática para ajudar no debug
            print(f"Linha não correspondente: {line.strip()}")

    # Criar um DataFrame com os dados
    df = pd.DataFrame({
        'Data': data_list,
        'Hora': hora_list,
        'Nome': nome_list,
        'Mensagem': mensagem_list
    })

    df.to_csv('whatsapp_conversa_tabela.csv', index=False)
    print("CSV criado com sucesso!")

