import csv

transacoes = [
    ["2026-03-15", "D", 150.00],
    ["2026-03-10", "C", 500.00],
    ["2026-03-15", "C", 150.00],
    ["2026-03-15", "D", 200.00],
]

def gerar_arquivo_bruto(nome_arquivo="transacoes_brutas.csv"):
    with open(nome_arquivo, mode="w", newline="", encoding"utf-8") as file:
        writer = csv.writer(file)
        writer.writerow(["data", "tipo", "valor"])