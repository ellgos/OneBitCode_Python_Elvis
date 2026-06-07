game_name = input("Digite o nome do Jogo: \n")
year_launch = int(input("Digite o ano de lançamento do jogo: \n"))
genre = input("Digite o gênero do jogo: \n")
price = float(input("Digite o preço do jogo: \n"))

# Alternativa 1
# print("\nInformações do Jogo:")
# print("Nome do Jogo:", game_name)
# print("Ano de Lançamento:", year_launch)
# print("Gênero:", genre)
# print("Preço:", price)

# Alternativa 2
# print("Nome do Jogo:", game_name,
#       "\nAno de lançamento:", year_launch,
#       "\nGenero do Jogo:", genre,
#       "\nPreço do Jogo:", price)

# ----------------------- ALTERNATIVA 3 ------------------------
# ------------------ Mais utilizada "fstring" ------------------

print(f"\nNome do jogo: {game_name} "
      f"\nAno de Lançamnento: {year_launch} "
      f"\nGenero: {genre} "
      f"\nPreço: {price}"
)
