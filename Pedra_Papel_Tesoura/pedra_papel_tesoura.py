import random
import os

jogada = ["pedra","papel","tesoura"]
cont_player = 0
cont_computador = 0

print("=" *39)
print("Bem vindo ao jogo Pedra, Papel, Tesoura")
print("=" *39)

def main_print():
    print("=" *39)
    print("\nPLACAR:")
    print(f"Você: {cont_player}")
    print(f"Computador: {cont_computador}")
    print("\n")
    print("Escolha seu lance:")
    print("0 - Pedra | 1 - Papel | 2 - Tesoura")

def select_move():
    return random.choice(jogada)

def get_player_move():
    while True:
        try:
            player_move = int(input())
            if player_move not in [0, 1, 2]:
                raise
            return jogada[player_move]

        except Exception as e:
            print(e)

def ganhador(p_move, c_move):
    global cont_computador, cont_player
    
    if p_move == "papel":
        if c_move == "pedra":
            cont_player +=1
            return "p"

    elif c_move == "tesoura":
            cont_computador +=1
            return "c"

    else:
        return "d"

    if p_move == "pedra":
        if c_move == "tesoura":
            cont_player +=1
            return "p"

    elif c_move == "papel":
            cont_computador +=1
            return "c"

    else:
        return "d"

    if p_move == "tesoura":
        if c_move == "papel":
            cont_player +=1
            return "p"

    elif c_move == "pedra":
            cont_computador +=1
            return "c"

    else:
        return "d"

again = 1
while again == 1:
    main_print()
    player_move = get_player_move()
    computer_move = select_move()
    winner = ganhador(player_move, computer_move)

    print("")
    print("=" *39)
    print(f"Sua jogada: {player_move}")
    print(f"Jogada do computador: {computer_move}")

    if winner == "p":
        print("Você venceu!")
    elif winner == "c":
        print("Você perdeu!")
    else:
        print("Empate!")
    print("=" *39)

    while True:
        print("Jogar novamente? 0 - SIM | 1 - NÃo")
        next = int(input())
        if next == 0:
            break
        elif next == 1:
            again = 0
            break

    os.system("cls")