import random
import os
import msvcrt

monkey_i = random.randint(1,19)
monkey_j = random.randint(1,19)
banana_i = random.randint(1,19)
banana_j = random.randint(1,19)
snake_i = random.randint(1,19)
snake_j = random.randint(1,19)
points = 0
lives = 3

while True:
    for i in range(21):
        for j in range(21):
            if i == monkey_i and j == monkey_j:
                print('🐒',end='')
            elif i == banana_i and j == banana_j:
                print('🍌',end='')
            elif i == snake_i and j == snake_j:
                print('🐍',end='')
            else:
                print('🌴',end='')
        print()
    print(f'Points - {points}')
    print(f'❤️ - {lives}')
    move = msvcrt.getwch().upper()
    if move == 'W':       
        monkey_i -= 1
    elif move == 'S':
        monkey_i += 1
    elif move == 'A':
        monkey_j -= 1
    elif move == 'D':
        monkey_j += 1
    elif move == 'Q':
        break
    
    if abs(monkey_i - snake_i) > abs(monkey_j - snake_j):
        if monkey_i < snake_i:
            snake_i -= 1
        elif monkey_i > snake_i:
            snake_i += 1       
    else:
        if monkey_j < snake_j:
            snake_j -= 1
        elif monkey_j > snake_j:
            snake_j += 1
    
    if monkey_i == banana_i and monkey_j == banana_j:
        banana_i = random.randint(1,19)
        banana_j = random.randint(1,19)
        points += 1
        
    if monkey_i == 21 or monkey_j == 21 or monkey_i < 0 or monkey_j < 0 or (snake_i == monkey_i and snake_j == monkey_j):
        lives -= 1
        monkey_i = random.randint(1,19)
        monkey_j = random.randint(1,19)
        snake_i = random.randint(1,19)
        snake_j = random.randint(1,19)
        
    if points == 10:
        os.system('cls')
        print('You are win. :)')
        break
    elif lives == 0:
        os.system('cls')
        print('Game over. :(')    
        break

    os.system('cls')