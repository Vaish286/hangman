import random

# List of 5 predefined words
word_list = ['apple', 'tiger', 'plane', 'chair', 'house']

# Choose a random word from the list
secret_word = random.choice(word_list)

# Create a display with underscores for each letter in the word
guessed_word = ['_'] * len(secret_word)

# Keep track of guessed letters and number of attempts
guessed_letters = []
max_attempts = 6
wrong_attempts = 0

print("Welcome to Hangman!")
print("Guess the word, one letter at a time.")

# Game loop
while wrong_attempts < max_attempts and '_' in guessed_word:
    print("\nWord: ", ' '.join(guessed_word))
    print("Wrong guesses left:", max_attempts - wrong_attempts)
    print("Guessed letters:", ', '.join(guessed_letters))
    
    guess = input("Enter a letter: ").lower()

    if len(guess) != 1 or not guess.isalpha():
        print("Please enter a single alphabet letter.")
        continue

    if guess in guessed_letters:
        print("You already guessed that letter.")
        continue

    guessed_letters.append(guess)

    if guess in secret_word:
        for i in range(len(secret_word)):
            if secret_word[i] == guess:
                guessed_word[i] = guess
        print("Good guess!")
    else:
        wrong_attempts += 1
        print("Wrong guess!")

# End of game
if '_' not in guessed_word:
    print("\nCongratulations! You guessed the word:", secret_word)
else:
    print("\nGame over! The word was:", secret_word)

