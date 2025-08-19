import pandas as pd

thigela = pd.read_csv('thigela.csv') # Comando padrão para ler o .csv

thigela["Data"] = pd.to_datetime(thigela["Data"], dayfirst=True, errors="coerce") # Converte a coluna Data para outro formato 

thigela["AnoMes"] = thigela["Data"].dt.to_period("M") # Pega somente ano-mês

mensagensMes = thigela.groupby("AnoMes")["Mensagem"].count().reset_index() # Agrupa por ano/mes e conta o índice de mensagens 

mesMovimentado = mensagensMes.iloc[mensagensMes["Mensagem"].idxmax()] # Pega a linha com maior número de mensagens

print(f"Mensagens por mês: \n{mensagensMes} \nMẽs mais movimentado: \n{mesMovimentado["AnoMes"]} {mesMovimentado["Mensagem"]}")
