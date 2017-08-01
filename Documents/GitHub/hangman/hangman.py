# list drawing of hangman
hangman = ["-","-","|","\n  |","\n  o","\n -","|","-","\n /"," \\"]

word = input("Enter your word:")
word_list = list(word)
answer_list = list(word)
guess_list = []
guessed_letters = []
wrong_guess_count = 0

for letter in word_list:
    guess_list.append("_ ")
print(''.join(guess_list))
while wrong_guess_count != len(hangman) and answer_list != guess_list:
    guess = input("\nGuess a letter:").lower()
    if len(guess) > 1 or not guess.isalpha():
        print("Invalid guess")
    elif guess in guessed_letters:
        print("You have already guessed this letter")
    else:
        guessed_letters.append(guess)
        letter_found = False
        for letter in word_list:
            if letter == guess:
                letter_found = True
                letter_index = word_list.index(letter)
                del guess_list[letter_index]
                # replace the letter with a blank str in word_list
                word_list.pop(letter_index)
                word_list.insert(letter_index, "")
                guess_list.insert(letter_index, letter)
        print("\n" + "".join(guess_list))
        if not letter_found:
            wrong_guess_count += 1
    print("\n" + "".join(hangman[:wrong_guess_count]))
            
if wrong_guess_count == len(hangman):
    print("\nYou have lost!")
else:
    print("\nCongratulations!")
