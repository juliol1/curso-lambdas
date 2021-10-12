import os
import random
import re
import unidecode


def word_gen():

    words = {}
    with open("./archivos/data.txt", "r", encoding="utf-8") as f:
        for index, value in enumerate(f):
            words[index] = value.strip('\n')
    num = random.randint(0, len(words))
    word = words.get(num)
    return word


def menu(lives, word, level, opportunity):

    print("El juego del ahorcado\n")
    print("Es tu oportunidad No. #" + str(opportunity))
    print("Tienes " + str(lives) + " vidas\n")
    print("Estas en el nivel: " + str(level))
    print(word + "\n")


def game(word, level, opportunity):

    answer = {}
    for index, letter in enumerate(word): 
        answer[index] = letter

    palabra = ["_" for letter in word]
    out = "".join(palabra)
    
    correct = True

    lives_left = 5
    
    
    while correct and lives_left > 0 :
        os.system("clear")
        menu(lives_left, out, level, opportunity)
        fin = "".join(palabra)
        try:
            in_letter = str(input("Ingresa una letra: "))
            if not re.search('[a-zA-Z]', in_letter):
                raise ValueError("Solo puedes ingresar letras")
        except ValueError as ve:
            in_letter = str(input("Ingresa un carácter válido: "))
        

        for index, value in enumerate(palabra):
            if unidecode.unidecode(answer[index]) == in_letter:
                palabra[index] = in_letter
            
        
        out = "".join(palabra)
        print(out + "\n")
        if unidecode.unidecode(out) == unidecode.unidecode(word):
            correct = False
            
        elif fin == out:
            lives_left -= 1
    
    if correct == False:
        os.system("clear")
        print(" Felicidades adivinaste la palabra\n" + word + "\n")
        new_game = input(""" Seguir jugando? [y/n] """)
        if new_game == 'y':
            return "new_game"
        elif new_game == 'n':
            os.system("clear")
            print("Juego Terminado\n")
            print("Llegaste al nivel: " + str(level))
            return False

    if lives_left == 0:
        os.system("clear")

        cont = input("""Continuar la partida? [y/n] """)

        if cont == 'y':
            return "cont"
        elif cont == 'n':
            print("""Perdiste, te quedaste sin vidas
            La palabra era """ + word)
            return False


def run():
    word = word_gen()
    nivel = 1
    op = 1
    cont = game(word, nivel, op)
    while cont:
        if cont == "cont":
            word = word
            op += 1
            cont = game(word, nivel, op)
        if cont == "new_game":
            word = word_gen()
            nivel += 1
            cont = game(word, nivel, op)


if __name__ == "__main__":
    run()