import random
import string

#open text file of words, save as a list and randomly select a word for play
def new_word():
        with open("words.txt", "r") as word_obj:
            contents = word_obj.read()
            words = contents.split()
            word = random.choice(words)
            return word

def letters_display(secret_word):        
        result = ["_"] * len(secret_word)
        print("Your new word has " + str(len(secret_word)) +" letters.")
        return result

def remaining_letters(used, alpha):
        if used in alpha:
                alpha.remove(used)
                return alpha
        else:
             print("\nOK DING-DONG! You have already used that letter -- try again!")

def hangman():
        alpha = list(string.ascii_lowercase)
        count = 6
        play_word = new_word()
        letters_list = list(play_word)
        result = letters_display(play_word)
        print(play_word)
        while letters_list != result:
            print("\nHere are the letters you have to choose from:")
            for letter in alpha:
                        print (letter, end="" + " ")

            guess = input("\n\nGuess a letter: ").lower()
                                           
            if guess not in string.ascii_lowercase or guess == "":
                print("Uh...Letter please!")
            elif guess in letters_list and guess in alpha:
                print("\nWOOT-WOOT!! You guessed a letter!\n")
                for index, char in enumerate(letters_list):
                    if char == guess:
                        result[index] = guess
                for char in result:
                    print (char, end=" ",)
                print("\n")
                remaining_letters(guess, alpha)
            elif count > 0 and guess in alpha:
                print("\nThat letter is not in the word. Try Again!")
                count -= 1
                remaining_letters(guess, alpha)
            elif count == 0:
                print ("\nHANGMAN!")
                print("The word was: " + play_word)
                play_again()
                break
            else:
                remaining_letters(guess, alpha)
        if letters_list == result:
            print("NICE JOB!! YOU WON!")
            play_again()
          
def play_again():
        play_again = input("Do you want to play again? Type 'y' for yes, 'n' for no: ")
        if play_again == 'y':
            hangman()
        else:
           quit
hangman()
            
        
         
  


    
