from turtle import Turtle, Screen
import random

screen = Screen()
screen.setup(width=1000, height=800)
user_bet = screen.textinput(title="Make your bet",
                            prompt="What Color Turtle do you think will win? (red/green/blue/yellow/orange)")
colors = ["red", "orange", "yellow", "green", "blue", "purple"]
turtle_y = [75, 45, 15, -15, -45, -75]
all_turtles = []

for turtle_index in range(0, 6):
    new_turtle = Turtle()
    new_turtle.shape("turtle")
    new_turtle.penup()
    new_turtle.color(colors[turtle_index])
    new_turtle.goto(-400, turtle_y[turtle_index])
    all_turtles.append(new_turtle)


def random_move(racer):
    racer.forward(random.randint(0, 20))


game_is_on = False

print(user_bet)

if user_bet:
    game_is_on = True

winner = ""

while game_is_on:
    for turtle_index in range(0, 6):
        random_move(all_turtles[turtle_index])
        if int(all_turtles[turtle_index].position()[0]) >= 500:
            winner = colors[turtle_index]
            game_is_on = False

if user_bet.lower() == winner:
    print(f"you won! {user_bet} won the race")
else:
    print(f"you lost! {winner} won the race not {user_bet}")

screen.exitonclick()
