import pandas as pd

thigela = pd.read_csv("thigela.csv")

thigela["Horário"] = thigela["Hora"]

thigela["Horário"] = pd.to_datetime(thigela["Horário"], format="%H:%M")

thigela["Tempo"] = thigela["Horário"].dt.hour

hora_moda = thigela["Tempo"].mode()[0]

print(f"Horário mais movimentado: {hora_moda}-{hora_moda+1}")