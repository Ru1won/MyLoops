print ("Hello world!")
person = input("What's your name?")
print ("Hello",person,)
print ('The object of the quiz is to get the least amount of points you can')
print ('If you answer a question correctly, you get 1 point...')
print ('If you answer a question incorrectly, you get 2 points.')
print ('DO NOT use capitals for any of your answers on this quiz')
def check_guess(guess1, answer):
    global score
    if guess1 == answer:
        print ('Correct answer!')
        score = score + 1
        print ('Your score is', score)
    else:
        print ('Try again')
        score = score + 2
        print ('Your score is', score)
        guess1 = input('Which country resides at the bottom of the world?')
        check_guess(guess1, 'antarctica')
score = 0
print ('Guess the country!')
guess1 = input('Which country resides at the bottom of the world?')
check_guess(guess1, 'antarctica')

