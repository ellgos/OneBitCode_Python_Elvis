# ============================================================
# Exercício 1.1: Média Notas
# ============================================================

# Escreva um programa que leia as quatro notas de um aluno, calcule a média e mostre a mensagem "Aprovado" se a média for maior ou igual a 7, ou "Reprovado" caso contrário.
import colorama
from colorama import Fore, Style

colorama.init(autoreset=True)

# Média de aprovação
media_aprovacao = 7.0

# Valores de entrada
# Aluno
print(colorama.Fore.YELLOW + "\n\n=== insira as informações do aluno ===")
aluno = input("Digite o nome do aluno: ")
turma = input("Digite a turma do aluno: ")

# Notas
print( colorama.Fore.CYAN + "\n\n=== insira as notas do aluno ===")
nota1 = float(input("Digite a primeira nota: "))
nota2 = float(input("Digite a segunda nota: "))
nota3 = float(input("Digite a terceira nota: "))
nota4 = float(input("Digite a quarta nota: "))

# Cálculo da média
print( colorama.Fore.MAGENTA + "\n\n=== calculando a média ===")
def calcular_media(n1, n2, n3, n4):
    return (n1 + n2 + n3 + n4) / 4

media = calcular_media(nota1, nota2, nota3, nota4)

# Verificação de aprovação
print(colorama.Fore.BLUE + "\n\n=== verificando aprovação ===")
def verificar_aprovacao(media, media_aprovacao):
    if media >= media_aprovacao:
        return colorama.Fore.GREEN + "Aprovado"
    else:
        return colorama.Fore.RED + "Reprovado"

resultado = verificar_aprovacao(media, media_aprovacao)

# Exibição do resultado
def exibir_resultado(aluno, turma, media, resultado):
    print(colorama.Fore.YELLOW + "\n\n=== RESULTADO ===")
    print(f"Aluno: {aluno}")
    print(f"Turma: {turma}")
    print(f"Média: {media:.2f}")
    print(f"Resultado: {resultado}")

exibir_resultado(aluno, turma, media, resultado)
