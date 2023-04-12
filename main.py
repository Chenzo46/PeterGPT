import tkinter,customtkinter
import gpt_backend
import os

customtkinter.set_appearance_mode('System')
customtkinter.set_default_color_theme('blue')

has_api_key = False

# Define app properties
app = customtkinter.CTk()
app.title("Peter Griffin Chat Room")
app.resizable(False,False)
app.geometry('450x650')

# Find and set app logo
base_folder = os.path.dirname(__file__)
icon_path = base_folder + '\images\peter_app_logo.png'
app_icon = tkinter.PhotoImage(file = icon_path)
app.iconphoto(False, app_icon)


# Main functions
def api_key_prompt():
    loading_indication.configure(text = 'Loading...')
    gpt_backend.ask_for_api_key()
    api_key_test = gpt_backend.api_key_works()
    if gpt_backend.get_api_key() != None and api_key_test:
        api_key_frame.destroy()
        show_main_chat_room()
    elif gpt_backend.get_api_key() == None:
        warn_user_api_key.configure(text = 'No API key was provided,\nplease try again...')
        loading_indication.configure(text = '')
    elif not api_key_test:
        warn_user_api_key.configure(text = 'Something went wrong while\nvalidating your API key.\nCheck that your API key is\nvalid, then try again.')
        loading_indication.configure(text = '')

def show_main_chat_room():
    main_frame.configure(width=400, height=600)

def send_user_prompt():
    user_prompt = user_entry.get()

    gpt_response = gpt_backend.generate_new_response(user_prompt)

    n_response = ''

    c_limit = 0
    for c in gpt_response:
        n_response += c
        if (not c.isalpha() and c not in " ',") or c_limit >= 50:
            n_response += '\n'
            c_limit = 0
        c_limit+=1

    conversation_frame.configure(text = n_response)

# Api key login frame
api_key_frame = customtkinter.CTkFrame(master = app, width=250, height=250, corner_radius=30)
api_key_frame.place(relx=0.5,rely=0.5,anchor=tkinter.CENTER)

# Ask user for api key to continue, if api key has been recieved, remove the button
warn_user_api_key = customtkinter.CTkLabel(master = api_key_frame, text = '', text_color='red', justify = 'center', text_font='biome')
warn_user_api_key.place(relx=0.5,rely=0.7,anchor=tkinter.CENTER)

loading_indication = customtkinter.CTkLabel(master = api_key_frame, text = '',  text_font='biome')
loading_indication.place(relx=0.5,rely=0.3,anchor=tkinter.CENTER)

api_key_button = customtkinter.CTkButton(master = api_key_frame, text = "Provide an API key to start...", hover=True, text_font='biome')
api_key_button.configure(command = api_key_prompt)
api_key_button.place(relx=0.5,rely=0.5,anchor=tkinter.CENTER)

# Main chat UI box
main_frame = customtkinter.CTkFrame(master = app, width=0, height=0)
main_frame.place(relx=0.5,rely=0.5,anchor=tkinter.CENTER)

# text box (User prompts + GPT responses)
conversation_frame = customtkinter.CTkLabel(master = main_frame, text = '', text_font='biome')
conversation_frame.place(relx=0.5,rely=0.7,anchor=tkinter.CENTER)

# User entry widget
user_entry = customtkinter.CTkEntry(master = main_frame, placeholder_text='Enter your prompt here...', width=350, text_font='biome')
user_entry.place(relx=0.45,rely=0.97,anchor=tkinter.S)

# PETER
base_folder = os.path.dirname(__file__)
icon_path = base_folder + '\images\peter_app_logo_in.png'
peter_icon = tkinter.PhotoImage(file = icon_path)
peter_image = tkinter.Label(main_frame, image=peter_icon)
peter_image.place(relx=0.5,rely=0.3,anchor=tkinter.CENTER)

# Button to submit user entry
base_folder = os.path.dirname(__file__)
icon_path = base_folder + '\images\submit_arrow_small.png'
submit_icon = tkinter.PhotoImage(file = icon_path)
submit_button = customtkinter.CTkButton(master = main_frame, image=submit_icon, text='', width=45, fg_color=None, hover_color='darkgrey', command = send_user_prompt)
submit_button.place(relx=0.94,rely=0.95,anchor=tkinter.CENTER)

app.mainloop()