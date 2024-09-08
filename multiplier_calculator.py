table = input ("What times table do you want me to repeat? (only numbers)")
multiplier = input ("What is your multiplier? (only numbers)")
y = 1
a = int(multiplier)
for counter in range (1,a+1):
    print (int(table) * y)
    y = y + 1
exitonclick()
