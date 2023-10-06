print('<Game Jokenpo>')
'''Game = PEDRA, PAPEL, TESOURA'''

while True:
    jogada1 = int(input(''' [1 - Jogador] \nEscolha \n0 - PEDRA\n1 - PAPEL\n2 - TESOURA \nDigite aqui -->'''))

    jogada2 = int(input(''' [2 - Jogador] \nEscolha \n0 - PEDRA\n1 - PAPEL\n2 - TESOURA \nDigite aqui -->'''))
    if jogada1 == jogada2:
        print("Empate")
    elif (jogada1 == 0 and jogada2 == 2) or (jogada1 == 1 and jogada2 == 0) or (jogada1 == 2 and jogada2 == 1):
        print("JOGADOR 1 VENCEU!")
    else:
        print("JOGADOR 2 VENCEU!")
    perg = input("JOGAR NOVAMENTE (s/n) ? ")
    if perg == 'n':
        break
print("Programa encerrado!")







