import random

def get_random():
    word_list = ["dog", "cat"]
    random_word = random.choice(word_list)

    return random_word.lower()

def play(random_word):
    real_word = "_" * len(random_word)  #shows the word as underlines
    guesses = 6 #number of incorrect guesses that can be given
    letters_guessed = [] #store the letters guessed so no duplicates
    finished = False #boolean for while loop so that I don't go infinite
    correct_letters = []
    wrong_letters = []
    print(real_word)
    while "_" in real_word and guesses > 0: #while true
        guess = (input("Guess a letter: ")).lower()
        if len(guess) == 1 and guess.isalpha(): #user can only guess one letter and it has to be in alphabet
            if guess in letters_guessed: #start with this because you want to append after
                print("You already guessed that letter, use a different letter")
            if guess in random_word:
                letters_guessed.append(guess) #add to letters guessed for the first conditional
                correct_letters.append(guess) #add letters to list of correct letters
                success = f'{guess} is in the word. Great job!'
                for char in range(len(random_word)):
                    if random_word[char] in correct_letters:
                        real_word = real_word[:char] + random_word[char] + real_word[char+1:] 
                print(success)
                print(real_word)
                print(wrong_letters)
            if guess not in random_word: #NOT GUARANTEED
                guesses -= 1 #decrement guesses so if guesses is 0, game ends
                letters_guessed.append(guess) #add to letters guessed for first conditional
                wrong_letters.append(guess) #append to wrong letters
                guesses_left = f'{guess} is not in word, you have {guesses} more guesses'
                print(guesses_left)
                print(wrong_letters)

            #if guesses == 0: #break for while loop so game ends
            #    break

            #finished = True #end the loop
            #loop terminates when guesses = 0 or when the word is complete 

   
                    
    if "_" not in real_word:
        print(f'Congratulations! The word was {random_word}') #win the game
    else: #or guesses = 0
        print(f'Sorry, the word was {random_word}') #lose the game

new = get_random()
play(new)


def new_game():
    while True:
        new_game = input("Play again? [Y/N]> ").lower()
        if new_game == "y":
            new = get_random()
            play(new)
        if new_game == "n":
            break
        else:
            print("Please type Y for a new game or N to finish")

new_game()