import csv

transacoes = []

with open("transacoes_brutas.csv", "r", encoding="utf-8") as arquivo:
reader = csv.DictReader(arquivo)

for linha in reader:
transacoes.append(linha)

transacoes.sort(key=lambda x: x["data"])

with open("transacoes_ordenadas.csv", "w", newline="", encoding="utf-8") as arquivo:
campos = ["data", "tipo", "valor"]

writer = csv.DictWriter(arquivo, fieldnames=campos)

writer.writeheader()
writer.writerows(transacoes)

print("Arquivo transacoes_ordenadas.csv gerado com sucesso!")