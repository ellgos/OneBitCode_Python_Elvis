# ============================================================
# Exercício 1: Antecessor e Sucessor Número
# ============================================================

# Escreva um programa que leia um número inteiro e mostre o seu antecessor e o seu sucessor.

numero = int(input("Digite um número inteiro: "))
antecessor = numero - 1
sucessor = numero + 1
print(f"O antecessor do número {numero} é {antecessor} e o sucessor é {sucessor}.")
print(f"{antecessor} <<< {numero} >>> {sucessor}")

