import turtle
import pandas

screen = turtle.Screen()
screen.title("India States Game")

image = "indian_political_img.gif"
screen.addshape(image)
turtle.shape(image)
screen.setup(width=600, height=600)

# def get_mouse_click_coor(x, y):
#     print(x, y)
# turtle.onscreenclick(get_mouse_click_coor)
# turtle.mainloop()

data = pandas.read_csv("28_states.csv")
all_state = data.state.to_list()



# If answer_state is one of the states in all the states of the 28_states.csv
guessed_state = []

while len(guessed_state) < 28:
    answer_state = screen.textinput(title=f"{len(guessed_state)}/28 States Correct", prompt="What's anther state's name?").title()
    if answer_state == "Exit":
        missing_states = []
        for state in all_state:
            if state not in guessed_state:
                missing_states.append(state)
        new_data = pandas.DataFrame(missing_states)
        new_data.to_csv("states_to_learn.csv")
        break

    if answer_state in all_state:
        guessed_state.append(answer_state)
        t = turtle.Turtle()
        t.hideturtle()
        t.penup()
        state_data = data[data.state == answer_state]
        t.goto(int(state_data.x), int(state_data.y))
        t.write(answer_state)


#states to learn.csv