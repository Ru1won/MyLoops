print ("Hello world!")
person = input("What's your name?")
print ("Hello",person,)
print ('DO NOT use capitals for any of your answers on this quiz.')
print ('If you answer a question correctly, you get 1 point...')
print ('If you answer a question incorrectly, you get 2 points.')
print ('The object of the quiz is to get the least amount of points you can.')
print ('Both the questions have different scores.')
print ('The total score will be shown at the end of the game.')
global score
score = 0
def check_guess(guess1, answer):
    global score
    if guess1 == answer:
        print ('Correct answer!')
        score = score + 1
        print ('Your score for the first question is', score)
        print ('================ End Of First Question ===============')
    else:
        print ('Try again.')
        score = score + 2
        print ('Your score for the first question is', score)
        guess1 = input('Which country resides at the bottom of the world?')
        check_guess(guess1, 'antarctica')
global SCORE
SCORE = 0
def check_guesstwo(guess2, answer):
    global SCORE
    if guess2 == answer:
        print ('Correct answer!')
        SCORE = SCORE + 1
        print ('Your score for the second question is', SCORE)
        print ('================ End Of Second Question ===============')
    else:
        print ('Try again.')
        SCORE = SCORE + 2
        print ('your score for the second question is', SCORE)
        guess2 = input('Which country was the homeland of lego?')
        check_guesstwo(guess2, 'denmark')
global Score
Score = 0
def check_guessthree(guess3, answer):
    global Score
    if guess3 == answer:
        print ('Correct answer!')
        Score = Score + 1
        print ('Your score for the second question is', Score)
        print ('================ End Of Third Question ===============')
        print ('Your total score is', SCORE + score + Score)
    else:
        print ('Try again.')
        Score = Score + 2
        print ('your score for the second question is', Score)
        guess3 = input('In which country does the Taj Mahal reside?')
        check_guessthree(guess3, 'india')
print ('Guess the country!')
guess1 = input('Which country resides at the bottom of the world?')
check_guess(guess1, 'antarctica')
guess2 = input('Which country was the homeland of lego?')
check_guesstwo(guess2, 'denmark')
guess3 = input('In which country does the Taj Mahal reside?')
check_guessthree(guess3, 'india')
