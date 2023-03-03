#This guy here generates words at  random
#One funny guy
def word_generator(z):
    with open("words.txt") as word_file:
        english_word = list(word.strip().lower() for word in word_file)

    import random

    number = random.randint(0, (len(english_word) - 1))
    item = english_word[number]
    while len(item) > z:
        number = random.randint(0, (len(english_word) - 1))
        item = english_word[number]
    scrabble_word = list(item)
    #Shake it very well lol
    scrabble_word_temp = scrabble_word[:]
    while scrabble_word_temp == scrabble_word:
        random.shuffle(scrabble_word)
    temp = (item, scrabble_word)
    return temp

#If hint word is in the dictionary give him, then he's not a liar
def hint_generator(x):
    with open("words.txt") as word_file:
        english_word = list(word.strip().lower() for word in word_file)
    if x in english_word:
        return True
    return False

#This prints the hint word for the user
def generate_hint(x):
    import random
    temp = ""
    switch = True
    number = random.randint(0, len(x) - 1)
    for n in x:
        if n == x[number] and switch == True:
            temp += n
            switch = False
        else:
            temp += "_"
    return temp
#This merges the hints generated 
def hint_merger(m, n):
    a = list(m)
    b = list(n)
    string = ""
    for i in range(0, len(a)):
        if a[i] != "_" and b[i] == "_":
            string += a[i]
        elif a[i] == "_" and b[i] != "_":
            string += b[i]
        else:
            string += "_"
    print (string)
    return string

    
#This function right here
#is used to make sure the hint word formed
#by the user can actually be gotten from the word.
#Yunno for saome smart folks :)
def compare(userword, actualword):
    x = list(userword)
    y = list(actualword)
    for z in x:
        if z in y:
            y.remove(z)
        else:
            return False
    return True         

#This function right here
#is used incase the user input all letters 
#to form word but missed the placings, &
#the new word formed is not in the dictionary :)
def equalletter(j, k):
    x = list(j) #userword list
    y = list(k) #actualword list
    for a in y:
        if a in x:
            x.remove(a)
    if x == []:
        return True
    return False



#Does what the name depicts
def play_again(x):
    while x not in ("y", "n"):
        x = input("Do You Want To Play Again [y / n]: ")
    return x

#Dont make me repeat myself
def end_game(y):
    print("\nThanks for playing !!!")
    print("Point:", y)


print("WELCOME TO WORD GAME")
print("Guess The Word Correctly & Earn Points\n")
print("-" * 40)
print("Instructions:")
print("-" * 40)
print("Get hint coins by forming extra words form the original word")
print("Hint coins are used to generate the position of letters in the original word")
print("You have only 3 chances")
print("Goodluck !!!")
#print("-" * 40)
print("-" * 80)
print("\nChoose Level")
print("(1) 3 Letter words and below")
print("(2) 5 Letter words and below")
print("(3) 7 Letter words and below\n")

difficulty = ""
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
    hintcoin = 0
    choice = "y"
    hint_word = []
    while choice == "y":
        print("\nThe word is: ", end="")
        health = 3
        hint_word_storage = []
        merge = []
        word = word_generator(s)
        for n in word[1]:
            print(n, sep="", end="")
            
        #Save Me...
        #Lol, this is where the real deal go down.
        #Don't tamper with :)
        print("\nHint Coin(s): ", hintcoin)
        while health >= 0:
            hint_choice = ""
            while hint_choice not in ("y", "n") and len(hint_word) < len(word[0]) and hintcoin >= 5:
                hint_choice = input("\nUse hint (y / n)? ")
            if hint_choice == "y":
                hintcoin -= 5
                temp_hint_word = generate_hint(word[0])
                while temp_hint_word in hint_word:
                    temp_hint_word = generate_hint(word[0])
                if len(hint_word) == 0:
                    print(temp_hint_word)
                    merge.append(temp_hint_word)
                else:
                    merge.append(hint_merger(temp_hint_word, merge[len(merge) - 1]))
                hint_word.append(temp_hint_word)
            if hint_choice == "y" and hintcoin < 5:
                print("No Hint Available")
            answer = input("\nGuess Word: ").lower().strip()
            if answer == word[0]:
                print("Correct!!")
                point += 10
                hint_word = []
                print("Points:", point)
                break
            elif hint_generator(answer) == True and answer != word[0] and compare(answer, word[0]) == True and len(answer) != 1 and answer not in hint_word_storage:
                if len(answer) <= 2:
                    hintcoin += 1.5
                    print("You got 1.5 hint coins")
                    hint_word_storage.append(answer)
                    print("Hint Coin(s):", hintcoin)
                else:
                    hintcoin += 3
                    print("You got 3 hint coins")
                    hint_word_storage.append(answer)
                    print("Hint Coin(s):", hintcoin)
            elif answer != word[0] and equalletter(answer, word[0]) == True and answer.isalpha() == True and len(answer) == len(word[0]) and hint_generator(answer) == False:
                health -= 1
                if health == 1:
                    print("***You Have", health, "Chance Left***")
                    continue
                elif health > 1:
                    print("***You Have", health, "Chances Left***")
                    continue
                else:
                    print("\nCorrect Word:", word[0])
                    print("Game Over")
                    end_game(point)
                    exit()
            else:
                continue
        choice = input("Do You Want To Play Again [y / n]: ")
        choice = play_again(choice)
        if choice == "y":
            print("v" * 80)
        if choice == "n":
            end_game(point)
            exit()


game()








