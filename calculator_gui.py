import tkinter as tk

window = tk.Tk()

window.title('My Calculator')
window.geometry('400x550')
window.config(bg="#000000")

expression_display = tk.Label(
    window,
    text='',
    font=('Arial', 30),
    bg="#f9f6f6",
    fg='black'
)
expression_display.pack()

display = tk.Label(
    window,
    text='0',
    font=('Arial', 30),
    bg="#f9f6f6",
    fg='black'
)

display.pack()

button_frame = tk.Frame(window, bg="#000000")
button_frame.pack()

buttons = [
    ['7', '8', '9', '+'],
    ['4', '5', '6', '-'],
    ['1', '2', '3', '*'],
    ['.', '0', '=', '/'],
    ['C']
]

num1 = None
opr = None
num2 = None
new_num = True

def number_click(number):
    global new_num
    current = display.cget("text")

    if new_num:
        display.config(text=number)
        new_num = False
    else:
        display.config(text=current + number)

def opr_click(op):
    global num1, opr, new_num

    current = float(display.cget("text"))

    if num1 is not None and opr is not None and not new_num:
        num2 = float(display.cget("text"))
        if opr == '+':
            num1 = num1 + num2
        elif opr == '-':
            num1 = num1 - num2
        elif opr == '*':
            num1 = num1 * num2
        elif opr == '/':
            if num2 == 0:
                display.config(text='Undefined')
                return
            else:
                num1 = num1 / num2
        
        if num1 == int(num1):
            num1 = int(num1)

        display.config(text=str(num1))

    else:
        num1 = current

    opr = op
    new_num = True
    expression_display.config(text=str(num1) + ' ' + opr)

def equal_click():
    global num1, opr, new_num
    if num1 is None or opr is None:
        return

    num2 = float(display.cget("text"))

    if opr == '+':
        result = num1 + num2
    elif opr == '-':
        result = num1 - num2
    elif opr == '*':
        result = num1 * num2
    elif opr == '/':
        if num2 == 0:
            result = 'Undefined'
        else:
            result = num1 / num2

    if result != 'Undefined' and result == int(result):
        result = int(result)

    display.config(text=str(result))
    expression_display.config(text='')
    num1 = result
    new_num = True

def decimal_click():
    current = display.cget("text")
    if '.' not in current:
        display.config(text=current + '.')

def clear_all():
    global num1, opr, num2, new_num

    num1 = None
    opr = None
    num2 = None
    new_num = True

    display.config(text='0')
    expression_display.config(text='')

for row in range(len(buttons)):
    for column in range(len(buttons[row])):

        button_text = buttons[row][column]

        if button_text == '.':
            command = decimal_click
        elif button_text in ['+', '-', '*', '/']:
            command = lambda op=button_text: opr_click(op)
        elif button_text == '=':
            command = equal_click
        elif button_text == 'C':
            command = clear_all
        else:
            command = lambda number=button_text: number_click(number)

        button = tk.Button(
            button_frame,
            text=button_text,
            font=('Arial', 20),
            width=5,
            command=command
        )

        button.grid(row=row + 1, column=column)

window.mainloop()