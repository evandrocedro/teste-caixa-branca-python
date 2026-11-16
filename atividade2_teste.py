def saque(valor, saldo, limite_credito):
    status = False
    if valor <= saldo:
        saldo = saldo - valor
        status = True
    elif valor <= limite_credito:
        limite_credito = limite_credito - valor
        status = True
    return status, saldo, limite_credito

# Caso de Teste 1: Saque dentro do saldo disponível
status, saldo, limite_credito = saque(400, 1000, 500)
print("--- CASO DE TESTE 01 ---")
print("Saque realizado?", status)
print("Saldo:", saldo)
print("Limite de crédito:", limite_credito)

# Caso de Teste 2: Valor excede o saldo, mas cabe no limite de crédito
status, saldo, limite_credito = saque(1200, 1000, 1500)
print("\n--- CASO DE TESTE 02 ---")
print("Saque realizado?", status)
print("Saldo:", saldo)
print("Limite de crédito:", limite_credito)

# Caso de Teste 3: Valor ultrapassa o saldo e o limite de crédito
status, saldo, limite_credito = saque(1200, 1000, 500)
print("\n--- CASO DE TESTE 03 ---")
print("Saque realizado?", status)
print("Saldo:", saldo)
print("Limite de crédito:", limite_credito)
