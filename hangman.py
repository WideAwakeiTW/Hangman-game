import random
import string

#open text file of words, save as a list and randomly select a word for play
with open("words.txt", "r") as word_obj:
    contents = word_obj.read()
    words = contents.split()
    play_word = random.choice(words)

print(play_word)

letters_list = list(play_word)
result = ["_"] * len(letters_list)

print("Your new word has " + str(len(letters_list)) +" letters.")
alpha = list(string.ascii_lowercase)
def remaining_letters(used):
        alpha.remove(used)
        return alpha
 
count = 6
while letters_list != result:
    print("\nHere are the letters you have to choose from:")
    for letter in alpha:
        print (letter, end="")
    guess = input("\n\nGuess a letter: ").lower()
    if guess in alpha:
        remaining_letters(guess)
    else:
        print("\nOK DING-DONG! You have already used that letter -- try again!")
        continue
        
    if guess in letters_list:
        print("\nCorrect! You guessed a letter!\n")

        for index, char in enumerate(letters_list):
            if char == guess:
                result[index] = guess
        for char in result:
            print (char, end=" ",)
        print("\n")

    elif count > 0:
        print("\nThat letter is not in the word. Try Again!")
        count -= 1
    elif count == 0:
        print ("\nHANGMAN!")
        print("The word was: " + play_word)
        break
if letters_list == result:
    print("YOU WON!")   

  


    
