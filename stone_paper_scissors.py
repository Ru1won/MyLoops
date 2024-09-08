from random import randint

wins_computer = 0
wins_player = 0

print ('This is a game of "rock, paper, scissors".')
print ('Please do not use capital letters for any of your answers in\
 this game.')

for counter in range (1,9):
    player = input ('please enter rock(r), paper(p), or scissors(s)')
    random_num = randint(1, 3)
    if random_num == 1:
        computer = 'r'
    elif random_num == 2:
        computer = 'p'
    else:
        computer = 's'
    print ('Player Is',player, 'vs', 'Computer Is', computer)
    if computer == 'p' and player == 'r':
        wins_computer = wins_computer + 1
        print ('Computer Wins!')
    elif computer == 'r' and player == 'r':
        print ('It Is A Tie.')
    elif computer == 's' and player == 'r':
        wins_player = wins_player + 1
        print ('Player Wins!')
    elif computer == 'p' and player == 'p':
        print ('It Is A Tie.')
    elif computer == 'r' and player == 'p':
        wins_player = wins_player + 1
        print ('Player Wins!')
    elif computer == 's' and player == 'p':
        wins_computer = wins_computer + 1
        print ('Computer Wins!')
    elif computer == 'p' and player == 's':
        wins_player = wins_player + 1
        print ('Player Wins!')
    elif computer == 'r' and player == 's':
        wins_computer = wins_computer + 1
        print ('Computer Wins!')
    elif computer == 's' and player == 's':
        print ('It Is A Tie.')
    else:
        print ('Error.')

if wins_computer > wins_player:
    print ('The Computer Wins The Ultimate Match!')
elif wins_player > wins_computer:
    print ('The Player Wins The Ultimate Match!')
else:
    print ('Nobody Wins.')
