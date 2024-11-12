# Faturamento de cada estado
faturamento = {
    'SP': 67836.43,
    'RJ': 36678.66,
    'MG': 29229.88,
    'ES': 27165.48,
    'Outros': 19849.53
}

# Calcular o faturamento total
total_faturamento = sum(faturamento.values())

# Calcular e exibir o percentual de cada estado
for estado, valor in faturamento.items():
    percentual = (valor / total_faturamento) * 100
    print(f"O percentual de representação de {estado} é: {percentual:.2f}%")
