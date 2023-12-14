from turtle import Turtle, Screen
import random as rd

is_race_on = False
screen = Screen()
screen.setup(width=500, height=400)
screen.bgcolor("light pink")
user_bet = screen.textinput(title="Make a bet", prompt="Which turtle will win the race? Enter a color: ")
colors = ["red", "orange", "yellow", "green", "blue", "purple"]
num = -100
all_turtle = []

for x in range(len(colors)):
    new_turtle = Turtle(shape="turtle")
    new_turtle.color(colors[x])
    new_turtle.penup()
    new_turtle.goto(x=-230, y=num)
    num += 40
    all_turtle.append(new_turtle)


if user_bet:
    is_race_on = True

while is_race_on:
    for turtle in all_turtle:
        if turtle.xcor() > 250:
            winning_color = turtle.pencolor()
            is_race_on = False
            if winning_color == user_bet:
                print(f"You've won! The {winning_color} turtle is the winner.")
            else:
                print(f"You've lost! The {winning_color} turtle is the winner.")

        random_distance = rd.randint(0, 10)
        turtle.forward(random_distance)


screen.exitonclick()