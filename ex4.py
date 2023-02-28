faturamento_mensal = {
    'SP': 67836.43,
    'RJ': 36678.66,
    'MG': 29229.88,
    'ES': 27165.48,
    'Outros': 19849.53,
}

total_faturamento = 0

for estado in faturamento_mensal:
    total_faturamento += faturamento_mensal[estado]

for estado in faturamento_mensal:
    percentual = ((faturamento_mensal[estado] / total_faturamento) * 100)
    print(f'{estado} : {percentual:.2f}%')