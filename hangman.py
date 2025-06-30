#CODEALPHA INTERNSHIP
#Domain : Python Programming
#TASK 1 : Hangman Game
#Submitted by : PARNITA



import random

# My Word list
words = ["apple", "banana", "grapes", "mango", "peach"]
word = random.choice(words)
guessed = []
tries = 6

print("Welcome to Hangman Game!")

while tries > 0:
    display = ""
    for letter in word:
        if letter in guessed:
            display += letter
        else:
            display += "_"
    print("Word:", display)

    if display == word:
        print("Congratulations! You guessed the word.")
        break

    guess = input("Guess a letter: ").lower()

    if guess in guessed:
        print("You already guessed that letter.")
    elif guess in word:
        guessed.append(guess)
        print("Correct!")
    else:
        guessed.append(guess)
        tries -= 1
        print("Wrong! Tries left:", tries)

if tries == 0:
    print("Game over! The word was:", word)
