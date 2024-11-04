def dash(real_world,letter_list):
    print(" ".join(letter_list))
    if real_world == "".join(letter_list):
        print("YOU WON!")
        return False

def guess(real_word, guess_letter):
    global errors
    if guess_letter in used_letters:
        return "This Letter was Already Used, Try Agian"

    else:
        if guess_letter in real_word:
            used_letters.append(guess_letter)
            sort(real_word,guess_letter)
            return "Correct Guess"

        else:
            used_letters.append(guess_letter)
            errors -= 1
            return f"Wrong Guess, You Have {errors} Chances Left"

def sort(real_word,guess_letter):
    global letter_list
    for i in range(len(real_word)):
        if real_word[i] == guess_letter:
            letter_list[i] = guess_letter
            dash(real_word,letter_list)

if __name__ == "__main__":
    #ITERABLES & CONSTANTS
    print("HANGAMAN:")
    real_word = "brother"
    letter_list = [" _ " for x in range(len(real_word))]
    dash(real_word,letter_list)
    errors = 8
    used_letters = []

    while True and errors != 0:
        guess_letter = input("Guess a Letter: ").lower()
        print(guess(real_word,guess_letter))

    print("Game Over, You Did Not Win")