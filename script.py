from random import sample
from time import sleep

game = []

print('-' * 39)
print('          JOGAR NA MEGA SENA         ')
print('-' * 39)

num_of_game = int(input('Quantos jogos você quer sortear? '))

print('-=' *5, f'Sorteando {num_of_game} jogos', '-=' *5)
for x in range(num_of_game):
  num = sample(range(1, 60), 6)
  game.append(num[:])
  num.clear()
  print(f'Jogo {x+1:>2}: {game[x]}')
  sleep(1)

print('-=' *7, 'BOA SORTE!!', '-=' *7)