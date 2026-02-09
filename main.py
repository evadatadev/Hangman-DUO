# --- IMPORTS ---
import random as rd
import utils.hangman_art as a
import utils.hangman_words as w


# --- START ---
    
print(a.welcome)

chosen_word = ""
language = ""

while language != "d" and language != "p":
    language = input("Tippe 'd' für Deutsch / Digite 'p' para portgues: \n")
    if language == "d":
        chosen_word = r.choice(w.word_list_de)
    elif language == "p":
        chosen_word = r.choice(w.word_list_bra)
    else:
        print("Fehler. Bitte versuche es nochmal. / Error. Repita, por favor.")

lives = 6

if language == "d":
    print(f'''
**********************************
****** Herzlich Willkommen! ****** 
****** Deine Leben: {lives} ******
**********************************
          ''')
else:
    print(f'''
********************************
********** Bem-vindo! **********
****** Sua vidas: {lives} ******
********************************
          ''')

# Generate as many blanks as letters

placeholder = ""

for item in range(len(chosen_word)):
    placeholder += "_ "

if language == "d":
    print(f"Gesuchtes Word: {placeholder}")
else:
    print(f"Palavra de busca: {placeholder}")

game_over = False
correct_letters = []

while not game_over:
    # Ask the user to guess a letter    
    if language == "d":
        guess = input("Rate einen Buchstaben: ").lower()
        if guess in correct_letters:
            print("\nDiesen Buchstaben hast du schon probiert.\n")
            # Check if the letter is in the word
    else:
        guess = input("Adivinhe uma letra: ").lower()
        if guess in correct_letters:
            print("\nVôce já tentou esta letra.\n")
            # Check if the letter is in the word
    display = ""
    for letter in chosen_word:                  # jede Runde baut das Display neu auf
        if letter == guess:                     # fügt guess dem Display zu und speichert ihn in Liste
            display += guess
            correct_letters.append(guess)
        elif letter in correct_letters:         # fügt alle Buchstaben, die in der Liste gespeichert sind, dem Display zu.
            display += letter
        else:
            display += "_"                      # fügt "_" dem Display zu, wenn guess nicht in Wort und nicht in Liste, e    

    if language == "d":
        if guess not in chosen_word:
            lives -= 1
            print(a.stages[lives])
            print(f"\n{guess} ist nicht im gesuchten Wort.\n")
    else:
        if guess not in chosen_word:
            lives -= 1
            print(a.stages[lives])
            print(f"\n{guess} não esta na palavra, que vôce está procurando.\n")
        
    if language == "d":
        print("Gesuchtes Wort: ", display)   
        print(a.stages[lives])
        print(f"****** DEINE LEBEN: {lives} / 6 ******")
        
        if lives == 0:
            game_over = True
            print(f"*********** VERLOREN ***********")
            print(f"Das gesuchte Wort war: {chosen_word}")
        if "_" not in display:
            print(f"*********** GEWONNEN ***********")
            game_over = True
    else:
        print("Palavra de busca: ", display)   
        print(a.stages[lives])
        print(f"******* SUA VIDAS: {lives} / 6 *******")     
        
        if lives == 0:
            game_over = True
            print(f"*********** PERDIDO ************")
            print(f"A palvra de busca: {chosen_word}")
        if "_" not in display:
            print(f"************ GANHO *************")
            game_over = True

    
   