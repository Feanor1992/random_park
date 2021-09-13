import random

parks = list(input('Park name {}: '. format(i + 1)) for i in range(6))
park_choice = random.randint(0, 5)
print(parks[park_choice])

