import sys
import random
import textwrap
import os
from termcolor import colored, cprint

screen_width = 100

def attack_likes():
  enemy_health = 40
# the menu
print('                   ')
print('        _____ __ __ _____ _____ _____ _____ _____ ')
print('       |  _  |  |  |_   _|  |  |     |     |   | |')
print('       |   __|_   _| | | |     |-   -|  |  | | | |')
print('       |__|    |_|   |_| |__|__|_____|_____|_|___| v0.1')
print('                   ')
print('+------------------------------------------------------------+')
print('                   ')
print('                     [1]PLAY[1]')
print('                     [2]INFO[2]')
print('                   [3]TUTORIAL[3]')
print('                     [4]QUIT[4]')
print('                   ')
print('+------------------------------------------------------------+')


while True:
  t = input(cprint('>>>', attrs = ['blink']))
  # input buttons
  if t == "4": sys.exit()
  if t == "2": print('This is a indie text based video game coded by Braden Maclemale!')
  if t == "3": print('The Tutorial is not Yet Ready')
  if t == "1": break

# character name stuff
while True:
  print('+------------------------------------------------------------+')
  print('                   ')
  e = input('Enter a Character Name Here:')
  print('                   ')
  print('+------------------------------------------------------------+')
  print('                   ')
  print('Is This Correct?, ' + e)
  print('                   ')
  print('+------------------------------------------------------------+')
  print('                   ')
  x = input('Answer YES[1] or N0[2]:')
  print('                   ')
  if x == "1": break

print('                   ')
print('Ok Lets Start Playing!')
print('                   ')
print('+------------------------------------------------------------+')



while True:
  t = input('>>>') 
  if t == "i": 
    print('                        ~~INVENTORY~~            ')
    print('                          | Sword |    ') 
    print('                          |  Bow  |   ') 
    print('                          --------- ')
    print('+------------------------------------------------------------+')
    print('                   ')

  if t == "w":
     print('You found a random creature in the wild!')

  


