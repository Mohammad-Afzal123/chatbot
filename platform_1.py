# theme_menu=['SandyBeach','Light brown 13','python','black','random']
import os
try:
    import PySimpleGUI as sg # type: ignore
except:
    os.system(f'cmd /c "pip install PySimpleGUI"')
    import PySimpleGUI as sg # type: ignore
try:
    import requests
except:
    os.system(f'cmd /c "pip install requests"')
    import requests


import openai

# Replace with your actual API key
openai.api_key = "sk-proj-skVZXNTjGZt7u0IbxICKT3BlbkFJAMxDCUJiL82GpkaW9hCD" 

def chat_with_gpt(prompt):
    """
    Sends a prompt to the GPT-3.5-turbo model and returns the response.
    """
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[{"role": "user", "content": prompt}]
    )
    return response.choices[0].message.content.strip()

# Define the layout
layout = [
    [sg.Text('You :'), sg.InputText(key='-INPUT-')],
    [sg.Button('Send'), sg.Button('Exit')],
    [sg.Output(size=(80, 20), key='-OUTPUT-')]
]

# Create the window
sg.theme("SandyBeach")
window = sg.Window('Chatbot', layout)

# Event loop
while True:
    event, values = window.read()

    if event == sg.WIN_CLOSED or event == 'Exit':
        break

    if event == 'Send':
        user_input = values['-INPUT-']
        if user_input.lower() in ["quit", "exit", "bye"]:
            break
        response = chat_with_gpt(user_input)
        print("bot:", response, end="")  # Print to the output element
        window['-INPUT-'].update('')  # Clear the input field

window.close()

