import turtle
import pandas

data = pandas.read_csv("50_states.csv")

screen = turtle.Screen()
screen.title("U.S. States Game")
image = "blank_states_img.gif"
screen.addshape(image)

turtle.shape(image)
print(data["state"])
state_list = data["state"].to_list()
guessed_state = []
game_is_over = False

print(state_list)


def remove_guessed_items():
    [state_list.remove(state_item) for state_item in guessed_state]
    missing_states = pandas.DataFrame(state_list)
    missing_states.to_csv("missed_states.csv")


while not game_is_over:
    answer_state = screen.textinput(
        title=f"{len(guessed_state)}/50 Guess the state",
        prompt="What's another state's name?",
    ).title()

    if answer_state == "Exit":
        remove_guessed_items()
        break

    def check_state(state):
        if len(guessed_state) != 50:
            if state in state_list:
                return True
            else:
                return False
        else:
            global game_is_over
            t = turtle.Turtle()
            t.penup()
            t.hideturtle()
            t.goto(-50, 0)
            t.write(arg="You win!", font=("Times", 40, "bold"))
            game_is_over = True

    if answer_state in guessed_state:
        print("Sorry, you have already Guessed that.")
    else:
        if check_state(answer_state):
            state = data[data["state"] == answer_state]
            xcor = int(state["x"])
            ycor = int(state["y"])
            t = turtle.Turtle()
            t.penup()
            t.hideturtle()
            t.setposition(xcor, ycor)
            t.write(arg=answer_state, align="center")
            guessed_state.append(answer_state)

        print(len(guessed_state))
        print(check_state(answer_state))


turtle.mainloop()
