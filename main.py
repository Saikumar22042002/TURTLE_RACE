from turtle import Turtle, Screen
import random
screen = Screen()

screen.setup(width =500,height = 500)
user_guess = screen.textinput(title ="Make your bet", prompt = "Which turtle will win the race ? choose colour:")
colours =["red","orange","yellow","green","blue","purple"]
y_position = [-100,-60,-20,20,60,100]
All_turtles =[]
for i in range(0,6):
    new_turtle = Turtle("turtle")
    new_turtle.penup()
    new_turtle.color(colours[i])
    new_turtle.goto(x = -230, y = y_position[i])
    All_turtles.append(new_turtle)

if user_guess:
    is_race = True

while is_race:
    for Turtle in All_turtles:
        if Turtle.xcor() > 230:
            is_race =False
            winning_colour = Turtle.pencolor()
            if winning_colour == user_guess:
                print(f"You've won.The {winning_colour} is Winner!")
            else:
                print(f"You've loss.The {winning_colour} is Winner!")

        random_distance = random.randint(0,10)
        Turtle.forward(random_distance)



screen.exitonclick()