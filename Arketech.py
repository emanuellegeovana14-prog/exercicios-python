 Arquivo: Credito_ArkeTech_NomeDaDupla.py
# Copiloto: ChatGPT

print("=== SISTEMA DE AUDITORIA DE CRÉDITO ARKETECH ===")

# Coleta de dados da empresa
nome_empresa = input("Digite o nome da empresa solicitante: ")
faturamento_mensal = float(input("Digite o faturamento mensal (R$): "))
valor_emprestimo = float(input("Digite o valor do empréstimo solicitado (R$): "))

# Cálculo da parcela mensal em 12 vezes, sem juros
parcela_mensal = valor_emprestimo / 12

# Cálculo do percentual da parcela em relação ao faturamento
percentual_faturamento = (parcela_mensal / faturamento_mensal) * 100

# Árvore de decisão para análise de crédito
if percentual_faturamento <= 30:
    parecer = "APROVADO"
    motivo = "A parcela compromete até 30% do faturamento mensal."

elif percentual_faturamento <= 50:
    parecer = "EM ANÁLISE (Risco Moderado)"
    motivo = "A parcela compromete entre 30% e 50% do faturamento mensal."

else:
    parecer = "RECUSADO"
    motivo = "A parcela compromete mais de 50% do faturamento mensal."

# Exibição do resultado usando f-strings
print("\n=== RESULTADO DA AUDITORIA ===")
print(f"Empresa solicitante: {nome_empresa}")
print(f"Faturamento mensal: R$ {faturamento_mensal:,.2f}")
print(f"Valor solicitado: R$ {valor_emprestimo:,.2f}")
print(f"Parcela mensal (12x): R$ {parcela_mensal:,.2f}")
print(f"Comprometimento do faturamento: {percentual_faturamento:.2f}%")
print(f"Parecer de crédito: {parecer}")
print(f"Motivo: {motivo}")