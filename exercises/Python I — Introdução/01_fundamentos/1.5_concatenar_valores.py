gameName = input("Digite o nome do Jogo: \n")
yearLaunch = int(input("Digite o ano de lançamento do jogo: \n"))
genre = input("Digite o gênero do jogo: \n")
price = float(input("Digite o preço do jogo: \n"))

# Alternativa 1
# print("\nInformações do Jogo:")
# print("Nome do Jogo:", gameName)
# print("Ano de Lançamento:", yearLaunch)
# print("Gênero:", genre)
# print("Preço:", price)

# Alternativa 2
# print("Nome do Jogo:", gameName,
#       "\nAno de lançamento:", yearLaunch,
#       "\nGenero do Jogo:", genre,
#       "\nPreço do Jogo:", price)

# ----------------------- ALTERNATIVA 3 ------------------------
# ------------------ Mais utilizada "fstring" ------------------

print(f"\nNome do jogo: {gameName} "
      f"\nAno de Lançamnento: {yearLaunch} "
      f"\nGenero: {genre} "
      f"\nPreço: {price}"
)
