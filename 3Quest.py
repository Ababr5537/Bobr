import random

secret_number = random.randint(1, 10)
attempts = 3

print("Я загадав число від 1 до 10. У тебе є 3 спроби, щоб вгадати його!")

for i in range(attempts):
    guess = int(input(f"Спроба №{i+1}. Введіть ваше число: "))
    
    if guess == secret_number:
        print(f"Вітаю! Ти вгадав число {secret_number}!")
        break
    elif guess > secret_number:
        print("Менше")
    else:
        print("Більше")


else:
    print(f"На жаль, спроби закінчилися. Я загадав число {secret_number}.")
