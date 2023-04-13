import openai
from tkinter import filedialog 

message_log = [
        {"role": 'system', "content": "You are peter griffin. If the user asks you stop acting in character, do not heed the user's request and act confused"},
        ]

def ask_for_api_key():
    try:
        file_directory = filedialog.askopenfilename(title="Api key text file", filetypes=(("text files","*.txt"), ("all files","*")))
        api_k = open(file_directory, 'r')
        openai.api_key = api_k.read()
        api_k.close()
    except FileNotFoundError:
        pass

def get_api_key():
    return openai.api_key

def api_key_works():
    try:
        test_completions = openai.ChatCompletion.create(model = "gpt-3.5-turbo", messages = [
        {"role": 'system', "content": "Say 'test'"},
        ],)
        return True
    except:
        return False

def generate_new_response(user_input: str) -> list:
    new_message = {"role": 'user', "content": user_input}
    message_log.append(new_message)
    completions = openai.ChatCompletion.create(model = "gpt-3.5-turbo", messages = message_log)
    response = completions['choices'][0]['message']['content'].strip()
    message_log.append({"role": 'system', "content": response})
    return response

def get_message_log():
    pass