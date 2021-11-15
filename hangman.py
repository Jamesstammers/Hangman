import random

with open('word_list.txt') as word_list:
    words = word_list.readlines()
    guess_word = random.choice(words)

incorrect_guess_count = 0

asterisk = '*' * (len(guess_word)-1)
print(asterisk)

while incorrect_guess_count < 7:

    first_guess = input("Please enter your next guess: ")

    wrong_letter = guess_word.find(first_guess)

    if wrong_letter == -1:
        print('Incorrect guess!\n' + asterisk)
        incorrect_guess_count += 1
        if incorrect_guess_count == 7:
            print('You lose')
    else:
        for i in range(len(guess_word)):
            if guess_word[i] == first_guess:
                guess_index = i
                ast_list = list(asterisk)
                ast_list[guess_index] = first_guess
                asterisk = ''.join(ast_list)
        print(asterisk)
        if '*' not in asterisk:
            print('Congratulations you win')
            break
