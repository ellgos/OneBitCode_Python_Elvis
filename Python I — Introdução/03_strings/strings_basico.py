
# ============================================================
# CRIAÇÃO E TIPOS DE STRING
# ============================================================

def tipos_de_string():
    simples    = 'Olá, mundo!'
    duplas     = "Python é incrível"
    multilinhas = """
        Isso é uma string
        com múltiplas linhas
    """
    raw = r"C:\Users\Elvis\documentos"   # raw string → ignora \n \t

    print("=" * 45)
    print("TIPOS DE STRING")
    print("=" * 45)
    print(f"Simples:     {simples}")
    print(f"Duplas:      {duplas}")
    print(f"Multilinha:  {multilinhas.strip()}")
    print(f"Raw string:  {raw}")


# ============================================================
# CONCATENAÇÃO E REPETIÇÃO
# ============================================================

def concatenacao():
    nome      = "Elvis"
    cargo     = "Analista"
    sistema   = "TJDFT"

    # Formas de concatenar
    texto_1 = nome + " — " + cargo + " no " + sistema   # concatenação direta
    texto_2 = f"{nome} — {cargo} no {sistema}"          # f-string (recomendado)
    texto_3 = "{} — {} no {}".format(nome, cargo, sistema)  # .format()
    separador = "-" * 45                                 # repetição

    print("\n" + "=" * 45)
    print("CONCATENAÇÃO")
    print("=" * 45)
    print(f"Direto:    {texto_1}")
    print(f"f-string:  {texto_2}")
    print(f"format():  {texto_3}")
    print(f"Repetição: {separador}")


# ============================================================
# LEN, INDEXAÇÃO E FATIAMENTO
# ============================================================

def indexacao():
    texto = "Python"
    #        P  y  t  h  o  n
    # índice: 0  1  2  3  4  5
    # negat.: -6 -5 -4 -3 -2 -1

    print("\n" + "=" * 45)
    print("INDEXAÇÃO E TAMANHO")
    print("=" * 45)
    print(f"Texto:            {texto}")
    print(f"Tamanho:          {len(texto)}")
    print(f"Primeiro char:    {texto[0]}")
    print(f"Último char:      {texto[-1]}")
    print(f"Índice 2:         {texto[2]}")


if __name__ == "__main__":
    tipos_de_string()
    concatenacao()
    indexacao()