# code here
import random
import json
# Adivinar la palabra por palabra
def guard_guess_word1(word_to_guess, word_guessed, letter, guessed_letters):
    if len(letter) != 1:
        raise ValueError("La entrada debe ser una letra.")
    if letter in guessed_letters:
        print(f"You already tried the letter '{letter}'.")
    else:
        guessed_letters.append(letter)
        for i in range(len(word_to_guess)):
            if letter == word_to_guess[i]:
                word_guessed[i] = word_to_guess[i]
                print("-------------------------\n")
                print("CORRECT\n")
                print("-------------------------\n")
        if "".join(word_guessed) == word_to_guess:
            print("¡Congratulations! ¡You guessed the word!")
        print(" ".join(word_guessed))
    return word_guessed, guessed_letters
 #guardar la palabra a adivinar y abrir json
def guard_word():
    with open("words.json", "r") as f:
        data = json.load(f)["data"]
        word = random.choice(data).lower()
        guess_word = ["_"] * len(word)
        print(" ".join(guess_word))
        return word,guess_word

#dibujar los errores
def print_hangman(attempts_left):
    stages = [
        """
           --------
           |      |
           |      O
           |     \|/
           |      |
           |     / \\
           -
        """,
        """
           --------
           |      |
           |      O
           |     \|/
           |      |
           |     / 
           -
        """,
        """
           --------
           |      |
           |      O
           |     \|/
           |      |
           |      
           -
        """,
        """
           --------
           |      |
           |      O
           |     \|
           |      |
           |     
           -
        """,
        """
           --------
           |      |
           |      O
           |      |
           |      |
           |     
           -
        """,
        """
           --------
           |      |
           |      O
           |    
           |      
           |     
           -
        """,
        """
           --------
           |      |
           |      
           |    
           |      
           |     
           -
        """
    ]
    print(stages[attempts_left])

# iniciar el juego
def play_hangman():
    while True:
        try:
            
            n = int(input("WOULD YOU LIKE TO START HANGMAN GAME? yes(1) or not(0): "))
            
            if n == 1:
                print("\tWELCOME TO HANGMAN GAME\n")
                print("-------------------------\n")
                print("You have 6 attempts to guess\n")
                print("YOUR WORD TO GUESS IS...\n")
                print("LET US BEGIN")
                word, guess_word = guard_word()
                attempts = 0
                max_attempts = 6
                guessed_letters = []
                #las opciones
                while attempts < max_attempts:
                    try:
                        print("\n<OPTIONS>")
                        print("1. Guess a letter")
                        print("2. Guess the whole word")
                        print("3. Exit the game")
                        user = int(input("CHOOSE AN OPTION: "))
                        # opcion 1 se conecta la funcion 1, guarda y actualiza 
                        if user == 1:
                            word_user = input("choose a character: ").lower()
                            guess_word, guessed_letters = guard_guess_word1(word, guess_word, word_user, guessed_letters)
                            if word_user not in word:
                                attempts += 1
                                print_hangman(max_attempts - attempts)
                                print(f"You have {max_attempts - attempts} attempts left.")
                                print("WRONG, KEEP TRYING")
                         #opcion 2 adivinar toda la palabra 
                        if user == 2:
                            word_user = input("guess the word: ").lower()
                            if word_user == word:
                                print("Congrats! You won.")
                                return word
                            else:
                                attempts += 1
                                print_hangman(max_attempts - attempts)
                                print(" ".join(guess_word))
                                print(f"You have {max_attempts - attempts} attempts left.")
                                print("WRONG, KEEP TRYING")
                         #salir del juego
                        if user == 3:
                            print("GAME OVER")
                            break
                    except ValueError:
                        print("Please choose again, the entered value was incorrect")
                if attempts == max_attempts:
                    print("You have run out of attempts. Game over.")
                    break
            elif n == 0:
                print("Goodbye!")
                break
            else:
                raise ValueError("Option must be either 1 or 0.")
        except ValueError:
            print("Error: Invalid input.")
play_hangman()
