import PySimpleGUI as sg


def window1():
    layout_1 = [[sg.Image(r'C:\Users\issac\OneDrive\Pictures\Pictures\love-yourself-j.png')],
                [sg.Text("This is a Self-Love App"), sg.Text(size=(15, 1), key='-OUT1-')],
                [sg.Text("Please click Start to continue."), sg.Text(size=(20, 1), key='-OUT2-')],
                [sg.Button('Start'), sg.Button('Exit')]]

    window_1 = sg.Window(title="Self-Love App", layout=layout_1, no_titlebar=True, alpha_channel=1, grab_anywhere=True)

    while True:
        event1, values1 = window_1.read()
        if event1 == 'Exit' or event1 == sg.WIN_CLOSED:
            break
        if event1 == 'Start':
            window2()

    window_1.close()


def window2():
    occupation = ('University Student', 'Employed', 'Unemployed', 'Retired')

    layout_2 = [[sg.Text('Please enter your name:')],
                [sg.InputText(key='-NAME-')],
                [sg.Text('Please enter your gender (Male/Female):')],
                [sg.InputText(key='-GENDER-')],
                [sg.Text('What is your current occupation?:')],
                [sg.Listbox(occupation, size=(18, len(occupation)), key='-OCCUPATION-')],
                [sg.Button('Next')]]

    window_2 = sg.Window(title='Questionnaires', layout=layout_2, no_titlebar=True, alpha_channel=1, grab_anywhere=True)

    while True:
        event2, values2 = window_2.read()
        if event2 == sg.WIN_CLOSED:
            break
        if event2 == 'Next':
            window_2.hide()
            window3()


def window3():
    multiple_choices1 = ('When you accomplish a project', 'When someone acknowledges you', 'By earning a lot of money',
                         'By leading others to success', 'Owning famous brands',
                         'Get the most/ special attention among the members')
    multiple_choices2 = (
        'Food', 'The latest technology', 'The latest fashion', 'Activities with friends', 'Home Improvements')
    multiple_choices3 = ('I make a chart or graph', 'Jotting it down on a scrap of paper', 'I talk to myself out loud',
                         'I write it down in my calendar', 'Any combination of these')
    multiple_choices4 = (
        'Dog', 'Cat', 'Fish', 'Bird', 'Snake', 'Hamster', 'Rabbit', 'Insects', 'Arachnids', 'Tortoise', 'Horse',
        'I am not a pet person')
    multiple_choices5 = ('Morning', 'Afternoon', 'Evening', 'Night')

    layout_3 = [[sg.Text('What boosts your confidence ? ')],
                [sg.Listbox(multiple_choices1, size=(45, len(multiple_choices1)), key='-MULTIPLE_CHOICES1-')],
                [sg.Text('I prefer to spend my money on.... ')],
                [sg.Listbox(multiple_choices2, size=(23, len(multiple_choices2)), key='-MULTIPLE_CHOICES2-')],
                [sg.Text('How do you organize your thoughts? Please pick whichever is closest. ')],
                [sg.Listbox(multiple_choices3, size=(35, len(multiple_choices3)), key='-MULTIPLE_CHOICES3-')],
                [sg.Text('Choose a pet which you prefer to keep. ')],
                [sg.Listbox(multiple_choices4, size=(18, len(multiple_choices4)), key='-MULTIPLE_CHOICES4-')],
                [sg.Text('What is your favorite time of the day? ')],
                [sg.Listbox(multiple_choices5, size=(15, len(multiple_choices5)), key='-MULTIPLE_CHOICES5-')],
                [sg.Button('Next')]]

    window_3 = sg.Window(title='Questionnaires', layout=layout_3, no_titlebar=True, alpha_channel=1, grab_anywhere=True)

    while True:
        event3, values3 = window_3.read()
        if event3 == sg.WIN_CLOSED:
            break
        if event3 == 'Next':
            window_3.hide()
            window4()


def window4():
    multiple_choices6 = ('The future', 'The past', 'Neither. I prefer the present')
    multiple_choices7 = (
        'Your future', 'Your family and friends', 'The state of the world', 'Money', 'How others see me')
    multiple_choices8 = (
        'Exactly where I live now', 'Overseas', 'In a small town', 'In a hectic big city', 'Cabin in the woods',
        'Traveling the world')
    multiple_choices9 = ('Green', 'Blue', 'Red', 'Yellow', 'Purple', 'White', 'Black')
    multiple_choices10 = (
        'By attending online courses', 'By attending lectures', 'By reading an e-Book', 'By reading a physical book',
        'By doing tutorial/lab questions', 'By doing assignments')

    layout_4 = [[sg.Text('Would you rather visit the future or the past? ')],
                [sg.Listbox(multiple_choices6, size=(20, len(multiple_choices6)), key='-MULTIPLE_CHOICES6-')],
                [sg.Text('What do you worry more about the most? ')],
                [sg.Listbox(multiple_choices7, size=(25, len(multiple_choices7)), key='-MULTIPLE_CHOICES7-')],
                [sg.Text('When you retire, you would like to live... ')],
                [sg.Listbox(multiple_choices8, size=(35, len(multiple_choices8)), key='-MULTIPLE_CHOICES8-')],
                [sg.Text('What is your favorite color? ')],
                [sg.Listbox(multiple_choices9, size=(15, len(multiple_choices9)), key='-MULTIPLE_CHOICES9-')],
                [sg.Text('What is your learning style? (Pick one that benefit you the most) ')],
                [sg.Listbox(multiple_choices10, size=(35, len(multiple_choices10)), key='-MULTIPLE_CHOICES10-')],
                [sg.Button('Next')]]

    window_4 = sg.Window(title='Questionnaires', layout=layout_4, no_titlebar=True, alpha_channel=1, grab_anywhere=True)

    while True:
        event4, values4 = window_4.read()
        if event4 == sg.WIN_CLOSED:
            break
        if event4 == 'Next':
            window_4.hide()
            window5()


def window5():
    layout_5 = [[sg.Text('Do you enjoy socializing with large groups of people?')],
                [sg.Slider(range=(1, 5), default_value=3, pad=(50, 0), orientation='horizontal', key='SLIDER1')],
                [sg.Text('I prefer to be alone             I yearn for human interaction')],
                [sg.Text('Do you enjoy challenges?')],
                [sg.Slider(range=(1, 5), default_value=3, pad=(50, 0), orientation='horizontal', key='SLIDER2')],
                [sg.Text('No, I like to take it easy             Yes, pain please!')],
                [sg.Text('How creative of a person do you think you are? ')],
                [sg.Slider(range=(1, 5), default_value=3, pad=(50, 0), orientation='horizontal', key='SLIDER3')],
                [sg.Text('Not creative at all                Leonardo Da Vinci')],
                [sg.Text('How logical of a person do you think you are? ')],
                [sg.Slider(range=(1, 5), default_value=3, pad=(50, 0), orientation='horizontal', key='SLIDER4')],
                [sg.Text('Not logic at all                     Albert Einstein')],
                [sg.Text('Would you prefer to engage your brain more than your body? ')],
                [sg.Slider(range=(1, 5), default_value=3, pad=(50, 0), orientation='horizontal', key='SLIDER5')],
                [sg.Text('I am more sporty                 I am more intellectual')],
                [sg.Text('Are you a curious person?')],
                [sg.Slider(range=(1, 5), default_value=3, pad=(50, 0), orientation='horizontal', key='SLIDER6')],
                [sg.Text('Not curious at all                 Extremely curious')],
                [sg.Text('Are you a perfectionist?')],
                [sg.Slider(range=(1, 5), default_value=3, pad=(50, 0), orientation='horizontal', key='SLIDER7')],
                [sg.Text('Everybody makes mistakes      Everything must be perfect')],
                [sg.Button('Next')]]

    window_5 = sg.Window(title='Questionnaires', layout=layout_5, no_titlebar=True, alpha_channel=1, grab_anywhere=True)

    while True:
        event5, values5 = window_5.read()
        if event5 == sg.WIN_CLOSED:
            break
        if event5 == 'Next':
            window_5.hide()
            window6()


def window6():
    layout_6 = [[sg.Text('Are you a trusting person?')],
                [sg.Slider(range=(1, 5), default_value=3, pad=(50, 0), orientation='horizontal', key='SLIDER8')],
                [sg.Text('I trust nobody                     I trust everyone!')],
                [sg.Text('Do you have lot of patience?')],
                [sg.Slider(range=(1, 5), default_value=3, pad=(50, 0), orientation='horizontal', key='SLIDER9')],
                [sg.Text('No patience at all                Extremely patient')],
                [sg.Text('Do you organize your schedule well? ')],
                [sg.Slider(range=(1, 5), default_value=3, pad=(50, 0), orientation='horizontal', key='SLIDER10')],
                [sg.Text('What schedule?            My schedule is very organized')],
                [sg.Text('Do you like to sit in front of a computer for long hours? ')],
                [sg.Slider(range=(1, 5), default_value=3, pad=(50, 0), orientation='horizontal', key='SLIDER11')],
                [sg.Text('    I hate it                                    I love it')],
                [sg.Text('Do you enjoy making others happy?')],
                [sg.Slider(range=(1, 5), default_value=3, pad=(50, 0), orientation='horizontal', key='SLIDER12')],
                [sg.Text('Others reactions               I am happy when ')],
                [sg.Text('do not affect me               everyone is happy!')],
                [sg.Text('Can you understand others perspectives and feelings?')],
                [sg.Slider(range=(1, 5), default_value=3, pad=(50, 0), orientation='horizontal', key='SLIDER13')],
                [sg.Text('Too complex to understand        I can read minds')],
                [sg.Text('How confident are you in your own abilities? ')],
                [sg.Slider(range=(1, 5), default_value=3, pad=(50, 0), orientation='horizontal', key='SLIDER14')],
                [sg.Text('Not confident at all           Extremely confident')],
                [sg.Button('Done')]]

    window_6 = sg.Window(title='Questionnaires', layout=layout_6, no_titlebar=True, alpha_channel=1, grab_anywhere=True)

    while True:
        event6, values6= window_6.read()
        if event6 == sg.WIN_CLOSED:
            break
        if event6 == 'Done':
            window_6.hide()
            output_element()


def output_element():
    '''layout_output = [[sg.Text('This is the output of your choices')],
                     [sg.Output(size=(45, 50), key='-OUTPUT-')],
                     [sg.Button('Check Your Result')]]

    window_output = sg.Window(title='Output', layout=layout_output, no_titlebar=True, alpha_channel=1,
                              grab_anywhere=True)'''

    while True:
        event7, values7 = window_output.read()
        if event7 == sg.WIN_CLOSED:
            break
        #window_output['-OUTPUT-'].update(values=window2().values['-NAME-'])
        if event7 == 'Check Your Result':
            window_output.close()
            '''Todo'''


def main():
    sg.theme('SystemDefault')
    window1()


if __name__ == '__main__':
    main()

#https://pysimplegui.readthedocs.io/en/latest/#pattern-1-a-one-shot-window-read-a-window-one-time-then-close-it
#https://pysimplegui.readthedocs.io/en/latest/cookbook/#recipe-printing
#https://pysimplegui.readthedocs.io/en/latest/call%20reference/#the-main-program-test-harness-global-settings-debug-information-upgrade-from-github
#https://github.com/PySimpleGUI/PySimpleGUI/issues/1633
