# Teste de Caixa Branca e Grafo de Fluxo (CFG)

Projeto desenvolvido para praticar técnicas de **Teste de Caixa Branca** em Python, aplicando análise de caminhos independentes e cálculo de complexidade ciclomática em uma operação de saque bancário.

## 1. Grafo de Fluxo de Controle (CFG) — Atividade 01

```mermaid
flowchart TD
    N1(("Nó 1: Início<br>status = False")) --> N2{"Nó 2: Decisão<br>valor <= saldo?"}
    N2 -- Verdadeiro --> N3["Nó 3: Sequência<br>saldo = saldo - valor<br>status = True"]
    N2 -- Falso --> N4{"Nó 4: Decisão<br>valor <= limite_credito?"}
    N4 -- Verdadeiro --> N5["Nó 5: Sequência<br>limite = limite - valor<br>status = True"]
    N4 -- Falso --> N6(("Nó 6: Convergência<br>return status, saldo, limite"))
    N3 --> N6
    N5 --> N6
```

### Complexidade Ciclomática
* **Nós (N):** 6
* **Arestas (E):** 7
* **Cálculo:** V(G) = E - N + 2 = 7 - 6 + 2 = **3 caminhos independentes**

---

## 2. Fluxo de Validação dos Casos de Teste — Atividade 02

```mermaid
flowchart LR
    Inicio(["Função saque(valor, saldo, limite)"]) --> CT1["CT 01: Saque 400 (Saldo 1000)<br>Caminho: 1 → 2 → 3 → 6<br>Retorno: True | Saldo: 600"]
    Inicio --> CT2["CT 02: Saque 1200 (Limite 1500)<br>Caminho: 1 → 2 → 4 → 5 → 6<br>Retorno: True | Limite: 300"]
    Inicio --> CT3["CT 03: Saque 1200 (Saldo 1000 / Limite 500)<br>Caminho: 1 → 2 → 4 → 6<br>Retorno: False | Sem alteração"]
```

### Tabela de Resultados Executados (`atividade2_teste.py`)

| Caso de Teste | Caminho Lógico | Entrada `(valor, saldo, limite)` | Saída Esperada `(status, saldo, limite)` |
| :--- | :--- | :--- | :--- |
| **CT 01** | `1 → 2 → 3 → 6` | `(400, 1000, 500)` | `(True, 600, 500)` |
| **CT 02** | `1 → 2 → 4 → 5 → 6` | `(1200, 1000, 1500)` | `(True, 1000, 300)` |
| **CT 03** | `1 → 2 → 4 → 6` | `(1200, 1000, 500)` | `(False, 1000, 500)` |
