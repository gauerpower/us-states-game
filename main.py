import turtle, pandas

scr = turtle.Screen()
scr.title('States Quiz Game')
scr.addshape('blank_states_img.gif')
turtle.shape('blank_states_img.gif')

states_data = pandas.read_csv('50_states.csv')
states_list = states_data.state.to_list()

correct_guesses = []

while len(correct_guesses) < 50:
    answer = scr.textinput(title = f'{len(correct_guesses)}/50 states correct', prompt = 'Type a state name, or type "Exit" to give up: ').title()
    mitch = turtle.Turtle()
    mitch.hideturtle()
    mitch.penup()
    if answer == 'Exit':
        incomplete_guesses_handler = open('incomplete_guesses.txt', 'w')
        message = ''
        for state in states_list:
            if state not in correct_guesses:
                message += f'{state}\n'
        incomplete_guesses_handler.write(message)
        incomplete_guesses_handler.close()
        break

    if answer in states_list and answer not in correct_guesses:
        matched_state_data = states_data[states_data.state == answer]
        mitch.goto(int(matched_state_data.iloc[0].x), int(matched_state_data.iloc[0].y))
        mitch.write(answer)
        correct_guesses.append(answer)

if len(correct_guesses) == 50:
    end_message = 'You guessed all 50 states correctly!'
else:
    end_message = 'Game over.\nView incomplete_guesses.txt file\nfor list of states you didn\'t know.'

mitch.goto(0, 0)
mitch.write(end_message, align='center', font = ('Times', 36, 'bold'))

turtle.mainloop()