
import random

num = random.randint(1, 20)
print(num)

while True:
    try:
        temp = int(input("Enter Number: "))
    except ValueError:
        continue
    else:
        break

if num == temp:
    print("CORRECT!!!")
else:
    print("Wrong")