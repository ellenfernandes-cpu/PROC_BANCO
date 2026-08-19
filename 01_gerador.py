import csv
import random
from datetime import datetime, timedelta

transacoes = []
data_inicial = datetime(2026, 1, 1)

# Geração dos dados
for i in range(20):
    data = data_inicial + timedelta(days=random.randint(0, 3))
    tipo = random.choice(["CREDITO", "DEBITO"])
    valor = round(random.uniform(10, 1000), 2)

    transacoes.append([data.strftime("%Y-%m-%d"), tipo, valor])

# Embaralha a lista completa apenas uma vez após o loop
random.shuffle(transacoes)

# Escrita no arquivo CSV
with open("transacoes_brutas.csv", "w", newline="", encoding="utf-8") as arquivo:
    writer = csv.writer(arquivo)
    writer.writerow(["data", "tipo", "valor"])
    writer.writerows(transacoes)

print("Arquivo transacoes_brutas.csv gerado com sucesso!")