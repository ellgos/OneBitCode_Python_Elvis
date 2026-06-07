# ============================================================
# OPERADORES ARITMÉTICOS
# ============================================================

def exemplos_aritmeticos():
    a = 10
    b = 3

    soma        = a + b    # 13
    subtracao   = a - b    # 7
    divisao     = a / b    # 3.333...
    divisao_int = a // b   # 3  → divisão inteira
    produto     = a * b    # 30
    modulo      = a % b    # 1  → resto da divisão
    potencia    = a ** b   # 1000

    print("=" * 40)
    print("OPERADORES ARITMÉTICOS")
    print("=" * 40)
    print(f"a = {a}, b = {b}")
    print(f"Soma:            {a} + {b}  = {soma}")
    print(f"Subtração:       {a} - {b}  = {subtracao}")
    print(f"Divisão:         {a} / {b}  = {divisao:.2f}")
    print(f"Divisão inteira: {a} // {b} = {divisao_int}")
    print(f"Produto:         {a} * {b}  = {produto}")
    print(f"Módulo (resto):  {a} % {b}  = {modulo}")
    print(f"Potência:        {a} ** {b} = {potencia}")


# ============================================================
# OPERADORES RELACIONAIS (COMPARAÇÃO)
# ============================================================

def exemplos_relacionais():
    x = 10
    y = 20

    print("\n" + "=" * 40)
    print("OPERADORES RELACIONAIS")
    print("=" * 40)
    print(f"x = {x}, y = {y}")
    print(f"x == y  (igual):           {x == y}")
    print(f"x != y  (diferente):       {x != y}")
    print(f"x >  y  (maior):           {x > y}")
    print(f"x <  y  (menor):           {x < y}")
    print(f"x >= y  (maior ou igual):  {x >= y}")
    print(f"x <= y  (menor ou igual):  {x <= y}")


# ============================================================
# EXEMPLO PRÁTICO — Calculadora simples
# ============================================================

def calculadora():
    print("\n" + "=" * 40)
    print("CALCULADORA SIMPLES")
    print("=" * 40)

    a = float(input("Digite o primeiro número: "))
    b = float(input("Digite o segundo número: "))

    print(f"\nSoma:            {a + b}")
    print(f"Subtração:       {a - b}")
    print(f"Multiplicação:   {a * b}")
    print(f"Divisão:         {a / b:.2f}" if b != 0 else "Divisão: ⚠️ Divisão por zero!")
    print(f"Potência a**b:   {a ** b}")
    print(f"Resto (a % b):   {a % b}" if b != 0 else "")

    print(f"\n{a} é maior que {b}? {a > b}")
    print(f"{a} é igual a {b}?  {a == b}")


if __name__ == "__main__":
    exemplos_aritmeticos()
    exemplos_relacionais()
    calculadora()