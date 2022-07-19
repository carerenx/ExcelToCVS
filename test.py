import tkinter
import tkinter.scrolledtext
from pynput import keyboard


def on_press(key, print_list):
    try:
        print_list.append('Alphanumeric key pressed: {0} '.format(key.char))
    except AttributeError:
        print_list.append('Special key pressed: {0}'.format(key))

def on_release(key, print_list):
    print_list.append('Key released: {0}'.format(key))
    print(print_list)
    # Stop the listener
    if key == keyboard.Key.esc:
        return False

def check_print():
    global print_list
    if print_list != []:
        for item in print_list:
            txt.insert(tkinter.END, item + "\n")
        print_list = []
    main.after(100, check_print)

# Main window
main = tkinter.Tk()
main.title('keyboad Logger')
main.geometry('500x400')


# Scrollable Textbox
print_list = ["fasf","fasdfsd","fadsgdsg"]
txt = tkinter.scrolledtext.ScrolledText(main, width = 40, height = 30)

# Insert into Textbox
txt.insert(tkinter.END, "Some text here")

txt.pack()

# Collect events until released
listener = keyboard.Listener(on_press=lambda key: on_press(key, print_list), on_release=lambda key: on_release(key, print_list), supress = True)
listener.start()
#
# check_print()


main.mainloop()