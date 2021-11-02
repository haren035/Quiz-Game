print('Welcome to my computer quiz!')

playing = input('Do you want to play? ')

if playing.lower() != 'yes':
    quit()

print("Okay! Let's play :)")
score = 0

answer = input("What does CPU stand for? ").lower()
if answer == "central processing unit" :
    score += 1
    print('COrrect!')
else:
    print('Incorrect')

answer = input("What does GPU stand for? ").lower()
if answer == "graphical processing unit" :
    score += 1
    print('Correct!')
else:
    print('Incorrect')

answer = input("What does RAM stand for? ").lower()
if answer == "random access unit" :
    score += 1
    print('Correct!')
else:
    print('Incorrect')

answer = input("What does PSU stand for? ").lower()
if answer == "power supply unit" :
    score += 1
    print('Correct!')
else:
    print('Incorrect')

print(f'you got {score} question correct ')

