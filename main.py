import turtle
import pandas

screen = turtle.Screen()
screen.title("U.S. States Game")
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)
on = True
data = pandas.read_csv("50_states.csv")
state_list = data.state.to_list()
total_states = []
while on:
    answer_state = str(screen.textinput(title=f"{len(total_states)}/50", prompt="What's another state's name?").title())
    if answer_state == "Exit":
        missing_states = [state for state in state_list if state not in total_states]
        new_data = pandas.DataFrame(missing_states)
        new_data.to_csv("remaining_states.csv")
        break
    if answer_state in state_list:
        state = data[data.state == answer_state]
        if answer_state not in total_states:
            total_states.append(answer_state)
        my_turtle = turtle.Turtle()
        my_turtle.hideturtle()
        my_turtle.penup()
        my_turtle.goto(int(state.x), int(state.y))
        my_turtle.write(f"{answer_state}", align="center", font=("Bold", 10, "normal"))
    if len(total_states) >= 50:
        on = False

