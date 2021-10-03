import random

while True:
    with open('Parks.txt', 'a+', encoding='utf-8') as parks_txt:
        for i_line in parks_txt.readlines():
            print(i_line, end='')

        parks = list(input('Park name {}: '. format(i + 1)) for i in range(6))
        park_choice = random.randint(0, 5)
        print()
        print(parks[park_choice])
        parks_txt.write(parks[park_choice] + '\n')

    if len(parks) == 6:
        print('программа сделала свой выбор')
        break
