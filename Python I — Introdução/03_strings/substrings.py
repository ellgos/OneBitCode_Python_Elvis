# ============================================================
# FATIAMENTO (SLICING)
# ============================================================

def fatiamento():
    texto = "Analista TJDFT"
    #        0123456789...

    print("=" * 45)
    print("FATIAMENTO DE STRINGS")
    print("=" * 45)
    print(f"Texto completo:         {texto}")
    print(f"texto[0:8]:             {texto[0:8]}")   # Analista
    print(f"texto[9:]:              {texto[9:]}")    # TJDFT
    print(f"texto[:8]:              {texto[:8]}")    # Analista
    print(f"texto[-5:]:             {texto[-5:]}")   # TJDFT
    print(f"Invertido texto[::-1]:  {texto[::-1]}")  # FDJTs atsylanA


# ============================================================
# BUSCA EM STRINGS
# ============================================================

def busca_em_strings():
    frase = "Elvis trabalha com automação em Python no TJDFT"

    print("\n" + "=" * 45)
    print("BUSCA EM STRINGS")
    print("=" * 45)
    print(f"Frase: {frase}")

    # in / not in
    print(f"\n'Python' está na frase?    {'Python' in frase}")
    print(f"'Java' está na frase?      {'Java' in frase}")
    print(f"'Java' não está na frase?  {'Java' not in frase}")

    # find() e index()
    pos_find  = frase.find("Python")    # retorna -1 se não encontrar
    pos_index = frase.index("TJDFT")    # lança erro se não encontrar

    print(f"\nPosição de 'Python':  {pos_find}")
    print(f"Posição de 'TJDFT':   {pos_index}")

    # count()
    vogais = frase.count("a")
    print(f"Qtd de 'a' na frase:  {vogais}")


# ============================================================
# VERIFICAÇÕES BOOLEANAS
# ============================================================

def verificacoes():
    print("\n" + "=" * 45)
    print("VERIFICAÇÕES")
    print("=" * 45)

    print(f"'Python'.startswith('Py'):  {'Python'.startswith('Py')}")
    print(f"'Python'.endswith('on'):    {'Python'.endswith('on')}")
    print(f"'12345'.isdigit():          {'12345'.isdigit()}")
    print(f"'Python'.isalpha():         {'Python'.isalpha()}")
    print(f"'  '.isspace():             {'  '.isspace()}")


if __name__ == "__main__":
    fatiamento()
    busca_em_strings()
    verificacoes()