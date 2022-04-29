''' Faça um programa que jogue par ou ímpar com o computador.
O jogo só será interrompido quando o jogador perder,
mostrando o total de vitórias consecutivas que ele conquistou,
no final do jogo.'''
import random
cont = r = 0
choose_player = choose_comp = ''

while True:
    player_choice = int(input('Escolha\n1-PAR\n2-IMPAR\n---> '))
    comp = random.randint(0, 10)
    player_choice_number = int(input('Digite um número entre 0 e 10: '))
    r = player_choice_number + comp
    if player_choice == 1:
        choose_player = 'PAR'
        choose_comp = 'IMPAR'
    else:
        choose_player = 'IMPAR'
        choose_comp = 'PAR'
    print(f'O computador escolheu {choose_comp} e você escolheu {choose_player} o resultado é {r}')
    if player_choice == 1 and r % 2 == 0 or player_choice == 2 and r % 2 != 0:
        print('Você ganhou! ')
        cont += 1
    else:
        print('Você perdeu! ')
        break
print(f'Você vendeu {cont} vezes. ')
