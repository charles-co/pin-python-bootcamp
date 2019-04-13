

def word_generator(z):
    with open("words.txt") as word_file:
        english_word = list(word.strip().lower() for word in word_file)

    import random

    number = random.randint(0, 370099)
    item = english_word[number]
    while len(item) > z:
        number = random.randint(0, 370099)
        item = english_word[number]
    scrabble_word = list(n for n in item)
    random.shuffle(scrabble_word)
    temp = (item, scrabble_word)
    return temp


def play_again(x):
    while x not in ("y", "n"):
        x = input("Do You Want To Play Again [y / n]: ")
    return x


def end_game(y):
    print("\nThanks for playing !!!")
    print("Point:", y)


print("WELCOME TO WORD GAME")
print("Guess The Word Correctly & Earn Points\n")
print("Choose Level")
print("(1) 3 Letter words and below")
print("(2) 5 Letter words and below")
print("(3) 7 Letter words and below\n")

difficulty = input("Enter Difficulty: ")
while difficulty not in ("1", "2", "3"):
    difficulty = input("Enter Difficulty: ")

if difficulty == "1":
    s = 3
elif difficulty == "2":
    s = 5
else:
    s = 7


def game():
    point = 0
    choice = "y"
    while choice == "y":
        print("\nThe word is: ", end="")
        health = 3
        word = word_generator(s)
#        print(word[0])
        for n in word[1]:
            print(n, sep="", end="")
        while health >= 0:
            answer = input("\nGuess Word: ")

            if answer == word[0]:
                print("Correct!!")
                point += 10
                print("Points:", point)
                break
            else:
                health -= 1
                if health == 1:
                    print("***You Have", health, "Chance Left***")
                    continue
                elif health > 1:
                    print("***You Have", health, "Chances Left***")
                    continue
                else:
                    print("\nCorrect Word: ", word[0])
                    print("Game Over")
                    end_game(point)
                    exit()
        choice = input("Do You Want To Play Again [y / n]: ")
        choice = play_again(choice)
        if choice == "n":
            end_game(point)
            exit()


game()







