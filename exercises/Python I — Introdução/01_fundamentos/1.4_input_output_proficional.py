# Exercício: Coleta de Dados do Jogador de forma PROFICIONAL!

# Função para coletar dados do jogador
def collect_player_data():
    """
    This Python function collects data about a player including their name, age, and favorite game.
    :return: A dictionary containing the player's name, age, and favorite game is being returned.
    """
    playerName = input("Nome do jogador: ")
    age = int(input("Idade do jogador: "))
    favoriteGame = input("Jogo favorito: ")

    return {
        "name": playerName,
        "age": age,
        "favoriteGame": favoriteGame
    }

# Exemplo de uso da função
# The code block `if __name__ == "__main__":` is a common Python idiom used to check if the current
# script is being run directly by the Python interpreter.
if __name__ == "__main__":
    player = collect_player_data()
    print("\nDados do jogador:")
    for key, value in player.items():
        print(f"{key}: {value}")
