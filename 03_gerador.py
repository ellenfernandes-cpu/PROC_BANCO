import csv

resumo = {}

# Leitura do arquivo ordenado e consolidação por data
with open("transacoes_ordenadas.csv", "r", encoding="utf-8") as arquivo:
    reader = csv.DictReader(arquivo)

    for linha in reader:
        data = linha["data"]
        tipo = linha["tipo"]
        valor = float(linha["valor"])

        if data not in resumo:
            resumo[data] = {"operacoes": 0, "creditos": 0.0, "debitos": 0.0}

        resumo[data]["operacoes"] += 1

        if tipo == "CREDITO":
            resumo[data]["creditos"] += valor
        elif tipo == "DEBITO":
            resumo[data]["debitos"] += valor

# Escrita do resumo diário no CSV
with open("resumo_diario.csv", "w", newline="", encoding="utf-8") as arquivo:
    campos = [
        "data",
        "quantidade_operacoes",
        "creditos",
        "debitos",
        "saldo",
    ]

    writer = csv.DictWriter(arquivo, fieldnames=campos)
    writer.writeheader()

    for data, valores in resumo.items():
        saldo = valores["creditos"] - valores["debitos"]

        writer.writerow(
            {
                "data": data,
                "quantidade_operacoes": valores["operacoes"],
                "creditos": round(valores["creditos"], 2),
                "debitos": round(valores["debitos"], 2),
                "saldo": round(saldo, 2),
            }
        )

print("Arquivo resumo_diario.csv gerado com sucesso!")