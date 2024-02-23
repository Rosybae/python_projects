# I addeded maximum number of guessing that will tell the user that he/she has exhausted the number of guesses. 
# But the game will continue playing until the right word is guessed correctly


print('Welcome to world guessing game')

secretWord = 'love'
userGuess = ''
guessCount = 0
maxGuesses = 4
hint = ' _ ' *len(secretWord)
print(f'Your hint is:{hint}')
while secretWord != userGuess:
    userGuess = input(' Please what is your guess? ').lower()
    guessCount += 1
    if secretWord == userGuess:
        print('Congratulations! You guessed it!')
        print(f'It took you {guessCount} number of guesses')
    elif len(secretWord) != len(userGuess):
        print('Sorry the guess must have same number of letters as the secret word')
        
        if userGuess.lower() != secretWord.lower() and guessCount == maxGuesses:
            print('You have used up all available guesses. Please try again with another word!')
    else:
        print('Your guess was incorrect!.')
        print(f"Your hint is:{hint}")
        for index, letter in enumerate(userGuess):
            if userGuess[index] == secretWord[index]:
                print(letter.upper(), end = ' ')
            elif letter in secretWord:
                print(letter.lower(), end = '')
            else:
                print('_', end = ' ') 