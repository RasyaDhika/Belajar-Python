import os
import re
import random
import string 
import pyfiglet

GBK = ['G','B','K']
judul = """|| Batu Gunting Kertas
|| Created : 10 Agustus 2022 // Kelas 8
"""
print(pyfiglet.figlet_format(judul))


while True:
    manusia = str(input('\n-- Pilih Senjata Anda ! Gunting[G], Batu[B], Kertas[K] : '))
    bot_choice =  random.choice(GBK)
    if manusia.upper() == 'G' and bot_choice == 'G':
        print('\n~ Yah Seri :(', '\n~ Pilihan lawan :',bot_choice.upper() + 'UNTING ✂️')
    elif manusia.upper() == 'K' and bot_choice == 'K':
        print('\n~ Kamu Menang !', '\n~ Pilihan lawan :',bot_choice.upper() + 'ERTAS 📃')
    elif manusia.upper() == 'B' and bot_choice == 'B':
        print('\n~ Kamu Menang !', '\n~ Pilihan lawan :',bot_choice.upper() + 'ATU 🪨')
    elif manusia.upper() == 'K' and bot_choice == 'B':
        print('\n~ Kamu Menang !', '\n~ Pilihan lawan :',bot_choice.upper() + 'ATU 🪨')    
    elif manusia.upper() == 'G' and bot_choice == 'K':
        print('\n~ Kamu Menang !', '\n~ Pilihan lawan :',bot_choice.upper() + 'ERTAS 📃')
    elif manusia.upper() == 'B' and bot_choice == 'G':
        print('\n~ Kamu Menang !', '\n~ Pilihan lawan :',bot_choice.upper() + 'UNTING ✂️')
    elif manusia.upper() == 'G' and bot_choice == 'B':
        print('\n~ LOL Kamu Kalah ^_^', '\n~ Pilihan lawan :',bot_choice.upper() + 'ATU 🪨')
    elif manusia.upper() == 'B' and bot_choice == 'K':
        print('\n~ LOL Kamu Kalah ^_^', '\n~ Pilihan lawan :',bot_choice.upper() + 'ERTAS 📃')
    elif manusia.upper() == 'K' and bot_choice == 'G':
        print('\n~ LOL Kamu Kalah ^_^', '\n~ Pilihan lawan :',bot_choice.upper() + 'UNTING ✂️')
    
