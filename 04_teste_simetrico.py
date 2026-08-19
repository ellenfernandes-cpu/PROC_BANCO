import csv

dados = [
    ["2026-01-01", "CREDITO", 100.00],
    ["2026-01-01", "DEBITO", 100.00],
    ["2026-01-02", "CREDITO", 200.00],
    ["2026-01-02", "DEBITO", 200.00],
    ["2026-01-03", "CREDITO", 300.00],
    ["2026-01-03", "DEBITO", 300.00],
    ["2026-01-04", "CREDITO", 400.00],
    ["2026-01-04", "DEBITO", 400.00],
]

with open("resumo_teste.csv", "w", newline="", encoding="utf-8") as arquivo:
    writer = csv.writer(arquivo)

    writer.writerow(
        ["data", "quantidade_operacoes", "creditos", "debitos", "saldo"]
    )

    for i in range(0, len(dados), 2):
        credito = dados[i]
        debito = dados[i + 1]

        saldo = credito[2] - debito[2]

        writer.writerow([credito[0], 2, credito[2], debito[2], saldo])

        if saldo == 0:
            print(f"{credito[0]}: SUCESSO - Saldo = {saldo:.2f}")
        else:
            print(f"{credito[0]}: ERRO - Saldo = {saldo:.2f}")