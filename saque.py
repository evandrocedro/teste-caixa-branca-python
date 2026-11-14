def saque(valor, saldo, limite_credito):
    status = False

    if valor <= saldo:
        saldo = saldo - valor
        status = True
    elif valor <= limite_credito:
        limite_credito = limite_credito - valor
        status = True

    return status, saldo, limite_credito

# Execução dos 3 caminhos independentes (Teste de Caixa Branca)
print("CT 01 (Caminho 1 -> 2 -> 3 -> 6):", saque(200, 500, 1000))
print("CT 02 (Caminho 1 -> 2 -> 4 -> 5 -> 6):", saque(700, 500, 1000))
print("CT 03 (Caminho 1 -> 2 -> 4 -> 6):", saque(1500, 500, 1000))
