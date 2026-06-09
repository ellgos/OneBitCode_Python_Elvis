# ============================================================
# MÉTODOS DE TRANSFORMAÇÃO
# ============================================================

def transformacao():
    texto = "  elvis gonçalves de siqueira  "

    print("=" * 45)
    print("TRANSFORMAÇÃO DE STRINGS")
    print("=" * 45)
    print(f"Original:      '{texto}'")
    print(f"upper():       '{texto.upper()}'")
    print(f"lower():       '{texto.lower()}'")
    print(f"title():       '{texto.title()}'")
    print(f"strip():       '{texto.strip()}'")
    print(f"lstrip():      '{texto.lstrip()}'")
    print(f"rstrip():      '{texto.rstrip()}'")
    print(f"capitalize():  '{texto.strip().capitalize()}'")


# ============================================================
# SUBSTITUIÇÃO E LIMPEZA
# ============================================================

def substituicao():
    texto = "Python é bom. Python é poderoso. Python é versátil."

    print("\n" + "=" * 45)
    print("SUBSTITUIÇÃO")
    print("=" * 45)
    print(f"Original:              {texto}")
    print(f"replace (1ª vez):      {texto.replace('Python', 'JS', 1)}")
    print(f"replace (todas):       {texto.replace('Python', 'JS')}")
    print(f"remove pontuação:      {texto.replace('.', '').replace(',', '')}")


# ============================================================
# SPLIT E JOIN
# ============================================================

def split_e_join():
    frase = "Elvis,Analista,TJDFT,Python,Automação"

    print("\n" + "=" * 45)
    print("SPLIT E JOIN")
    print("=" * 45)

    # split → string vira lista
    lista = frase.split(",")
    print(f"Original:  {frase}")
    print(f"split(',') → {lista}")
    print(f"Tipo:      {type(lista)}")

    # join → lista vira string
    juntado = " | ".join(lista)
    print(f"join(' | '): {juntado}")

    # Caso real: processar CSV simples
    linha_csv = "001,Elvis,Analista,TJDFT,Python"
    campos = linha_csv.split(",")
    print(f"\nCSV parseado: {campos}")
    print(f"Nome: {campos[1]} | Cargo: {campos[2]}")


# ============================================================
# F-STRINGS AVANÇADAS
# ============================================================

def fstrings_avancadas():
    nome   = "Elvis"
    salario = 8750.5
    nivel  = 3
    ativo  = True

    print("\n" + "=" * 45)
    print("F-STRINGS AVANÇADAS")
    print("=" * 45)
    print(f"Nome:          {nome}")
    print(f"Salário:       R$ {salario:,.2f}")        # formatação numérica
    print(f"Nível:         {nivel:02d}")              # zero à esquerda
    print(f"Ativo:         {ativo}")
    print(f"Maiúsculo:     {nome.upper()}")           # método dentro da f-string
    print(f"Expressão:     {2 ** 10}")                # expressão dentro da f-string
    print(f"Condicional:   {'Ativo' if ativo else 'Inativo'}")


if __name__ == "__main__":
    transformacao()
    substituicao()
    split_e_join()
    fstrings_avancadas()