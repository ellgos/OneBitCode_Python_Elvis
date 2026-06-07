'''
Exercício 3: Entrada de Dados

gameName = "Resident Evil 4 Remake"
yearLaunch = 2023
genre = "Survival Horror"
price = 249.99
playerName = "Leon S. Kennedy"
playerLevel = 15
isAlive = True

'''
# Solicita ao usuário que insira o nome do jogo
game_name = input("Digite o nome do Jogo: \n")
year_launch = int(input("Digite o ano de lançamento do jogo: \n"))
genre = input("Digite o gênero do jogo: \n")
price = float(input("Digite o preço do jogo: \n"))
player_name = input("Digite o nome do jogador: \n")
player_level = int(input("Digite o nível do jogador: \n"))
isAlive_input = input("O jogador está vivo? (s/n): \n")
isAlive = isAlive_input.lower() == 's'

# Exibe as informações coletadas
print("\nInformações do Jogo:")
print("Nome do Jogo:", game_name)
print("Ano de Lançamento:", year_launch)
print("Gênero:", genre)
print("Preço:", price)
print("\nInformações do Jogador:")
print("Nome do Jogador:", player_name)
print("Nível do Jogador:", player_level)
print("Está vivo?", isAlive)


