import random

#open text file of words, save as a list and randomly select a word for play
with open("words.txt", "r") as word_obj:
    contents = word_obj.read()
    words = contents.split()
    play_word = random.choice(words)

#creat blanks for letters to fill in for guesses




#check if guessed letter is in the play word
print(play_word)

##def new_game():
letters_list = list(play_word)
result = ["_"] * len(letters_list)
while letters_list != result:
    guess = input("Guess a letter: ").lower()
    print(letters_list, result)
    if guess in letters_list:
        print("you guessed a letter!")
    ##  FOR LOOP WILL ONLY REPLACE FIRST MATCH OF CHAR -- DONT USE!
    ##    for char in letters_list:
    ##        if char == guess:
    ##            i = letters_list.index(guess)
    ##            result[i] = guess

    ## EMUMERATE METHOD WILL FIND ALL INSTANCES OF CHAR
        for index, char in enumerate(letters_list):
            if char == guess:
                print(index)
                result[index] = guess
        print (result)
    else:
        print("That letter is not in the word. Try Again!")
print("YOU WON!")
            


##new_game()

  


    
