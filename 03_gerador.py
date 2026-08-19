import csv

resumo = {}

with open("transacoes_ordenadas.csv", "r", encoding="utf-8") as arquivo:
reader = csv.DictReader(arquivo)

for linha in reader:
data = linha["data"]
tipo = linha["tipo"]
valor = float(linha["valor"])

if data not in resumo:
resumo[data] = {
"operacoes": 0,
"creditos": 0,
"debitos": 0
}

resumo[data]["operacoes"] += 1

if tipo == "CREDITO":
resumo[data]["creditos"] += valor

elif tipo == "DEBITO":
resumo[data]["debitos"] += valor


with open("resumo_diario.csv", "w", newline="", encoding="utf-8") as arquivo:

campos = [
"data",
"quantidade_operacoes",
"creditos",
"debitos",
"saldo"
]

writer = csv.DictWriter(arquivo, fieldnames=campos)

writer.writeheader()

for data, valores in resumo.items():

saldo = valores["creditos"] - valores["debitos"]

writer.writerow({
"data": data,
"quantidade_operacoes": valores["operacoes"],
"creditos": valores["creditos"],
"debitos": valores["debitos"],
"saldo": saldo
})

print("Arquivo resumo_diario.csv gerado com sucesso!")