import random

while True:
    parks = list(input('Park name {}: '. format(i + 1)) for i in range(6))
    park_choice = random.randint(0, 5)
    print()
    print(parks[park_choice])

    if len(parks) == 6:
        print('программа сделал свой выбор')
        break
