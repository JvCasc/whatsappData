import pandas as pd
import re


path = r'thigela.txt'

# Abrir o arquivo exportado do WhatsApp
with open(path, 'r', encoding='utf-8') as file:
    lines = file.readlines()

# Inicializar listas para armazenar data, hora, nome e mensagens
data_list = []
hora_list = []
nome_list = []
mensagem_list = []

# Regex para capturar as partes da mensagem
pattern = r'(\d{2}/\d{2}/\d{4})\s(\d{2}:\d{2})\s-\s(.*?):\s(.*)'

# Processar cada linha da conversa
for line in lines:
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

# Verificar se o DataFrame tem dados
if df.empty:
    print("Nenhuma mensagem foi extraída. Verifique o formato do arquivo.")
else:
    # Salvar o DataFrame em um arquivo CSV ou Excel
    df.to_csv('whatsapp_conversa_tabela.csv', index=False)
    print("CSV criado com sucesso!")
    # Ou, se preferir um arquivo Excel:
    # df.to_excel('whatsapp_conversa_tabela.xlsx', index=False)
