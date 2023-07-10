import tkinter as tk
from tkinter import ttk

# window
window = tk.Tk()

width = 800
height = 600
window_width = window.winfo_screenwidth()
window_height = window.winfo_screenheight()
center_width = int(window_width / 2 - width / 2)
center_height = int(window_height / 2 - height / 2)

window.title('Bretto')
window.configure(background = '#999999')

window.geometry(f'{width}x{height}+{center_width}+{center_height}')

window.resizable(False, False)

# functions
def validate_input(P):

    if P == '' or P.isdigit() or P == '.':
        return True
    elif P.count(".") == 1 and P.replace(".", '').isdigit():
        return True
    else:
        return False

def to_gross_func():
    try:
        value1 = float(entry1.get())
        value2 = float(entry2.get())

        result = round((value1 * (value2/100 + 1)),2)

        label5.config(text = str(result))
    except ValueError:
        label5.config(text = 'Empty value(s)')
        
def to_net_func():
    try:
        value1 = float(entry1.get())
        value2 = float(entry2.get())
        
        result = round((value1 * (100/(100 + value2))),2)
        
        label5.config(text = str(result))
    except ValueError:
        label5.config(text = 'Empty value(s)')

# classes    
class CreateLabel:
    def __init__(self, window):
        self.window = window
    
    def create_widget(self, label_text, font_size):
        label = ttk.Label(
            self, 
            text = label_text, 
            font = ('Arial', font_size, 'bold'), 
            anchor = 'center')
        return label

class CreateEntry:
    def __init__(self, window):
        self.window = window
        
    def create_widget(self, font_size):
        entry = ttk.Entry(
            self,
            validate = 'key',
            validatecommand = (window.register(validate_input), '%P'), 
            font = ("Arial", font_size, 'bold'), 
            justify = 'center')
        return entry
 
class CreateButton:
    def __init__(self, window):
        self._window = window
    
    def create_widget(self, button_text, function):
        button = ttk.Button(
            self,
            text = button_text,
            command = function)
        return button
   
# widgets
label1 = CreateLabel.create_widget(window, 'NET/GROSS CALCULATOR', 20)
label2 = CreateLabel.create_widget(window, 'Value', 12)
label3 = CreateLabel.create_widget(window, 'VAT [%]', 12)
label4 = CreateLabel.create_widget(window, 'Result', 12)
label5 = CreateLabel.create_widget(window, 'Your result', 16)
label6 = CreateLabel.create_widget(window, 'Choose option', 12)

entry1 = CreateEntry.create_widget(window, 20)
entry2 = CreateEntry.create_widget(window, 20)

button1 = CreateButton.create_widget(window, 'To net [n]', to_gross_func)
button2 = CreateButton.create_widget(window, 'To gross [g]', to_net_func)

# grid
window.columnconfigure((0,1,2,3,4), weight = 1, uniform = 'a')
window.rowconfigure(0, weight = 1, uniform = 'a')
window.rowconfigure(1, weight = 1, uniform = 'a')
window.rowconfigure((2,3,4), weight = 1, uniform = 'a')

# layout
label1.grid(row = 0, column = 0, columnspan = 5, ipadx = 30, pady = (30, 0), ipady = 20)
label2.grid(row = 1, column = 0, sticky = 'we', padx = 10, ipady = 5)
label3.grid(row = 1, column = 1, sticky = 'we', padx = 10, ipady = 5)
label4.grid(row = 3, column = 1, columnspan = 3, ipadx = 100, ipady = 15)
label5.grid(row = 4, column = 1, sticky = 'we', columnspan = 3, ipadx = 10, pady = (0, 30), ipady = 30)
label6.grid(row = 1, column = 3, columnspan = 2, sticky = 'we', padx = 10, ipady = 10)

entry1.grid(row = 2, column = 0, sticky = 'nsew', padx = 10)
entry2.grid(row = 2, column = 1, sticky = 'nsew', padx = 10)

button1.grid(row = 2, column = 3, sticky = 'nsew', padx = 10)
button2.grid(row = 2, column = 4, sticky = 'nsew', padx = 10)

# events
window.bind('<Escape>', lambda event: window.quit())
window.bind('<n>', lambda event: to_net_func())
window.bind('<g>', lambda event: to_gross_func())

# run
window.mainloop()