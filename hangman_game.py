import random
from stage import stages, logo
from words import word_list

end_game = False

# word_list = ["karthi", "hero", "programmer", "ceo"]
chosen_word = random.choice(word_list)
print(chosen_word)

lives = 7

display = []
word_length = len(chosen_word)
for _ in range(word_length):
    display += "_"
print(display)

print(logo)

while not end_game:
    guess = input("Guess a Letter?\n").lower()

    for position in range(word_length):
        letter = chosen_word[position]
        if letter == guess:
            display[position] = letter

    print(display)
    if guess in display:
        print(f"You've already guess: {guess}")

    if guess not in chosen_word:
        lives -= 1
        if lives == 0:
            end_game = True
            print("You lose")

    if "_" not in display:
        end_game = True
        print("You win!")

    print(stages[lives])



