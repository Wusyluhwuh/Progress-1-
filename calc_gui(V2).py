import customtkinter as ctk

# Theme and appearance
ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("blue")

window = ctk.CTk()

window.title('My Calculator')
window.geometry('380x520')
window.resizable(False, False)

# Top display
expression_display = ctk.CTkLabel(
    window,
    text='',
    font=('Arial', 18),
    text_color='gray',
    anchor='e'
)
expression_display.pack(fill='x', padx=20, pady=(20, 0))

# Main calculation display
display = ctk.CTkLabel(
    window,
    text='0',
    font=('Arial', 36, 'bold'),
    anchor='e'
)
display.pack(fill='x', padx=20, pady=(0, 20))

button_frame = ctk.CTkFrame(window, fg_color="transparent")
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


def get_display_value():
    """Safely retrieves float value from display."""
    val = display.cget("text")
    if val == 'Undefined':
        return 0.0
    try:
        return float(val)
    except ValueError:
        return 0.0


def number_click(number):
    global new_num
    current = display.cget("text")

    if new_num or current == 'Undefined':
        display.configure(text=number)
        new_num = False
    else:
        display.configure(text=current + number)


def opr_click(op):
    global num1, opr, new_num

    current = get_display_value()

    if num1 is not None and opr is not None and not new_num:
        num2 = current
        if opr == '+':
            num1 = num1 + num2
        elif opr == '-':
            num1 = num1 - num2
        elif opr == '*':
            num1 = num1 * num2
        elif opr == '/':
            if num2 == 0:
                display.configure(text='Undefined')
                num1 = None
                opr = None
                new_num = True
                return
            else:
                num1 = num1 / num2

        if num1 is not None and num1 == int(num1):
            num1 = int(num1)

        display.configure(text=str(num1))
    else:
        num1 = current

    opr = op
    new_num = True
    expression_display.configure(text=f"{num1} {opr}")


def equal_click():
    global num1, opr, new_num
    if num1 is None or opr is None:
        return

    num2 = get_display_value()

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

    if result != 'Undefined':
        if result == int(result):
            result = int(result)
        display.configure(text=str(result))
        num1 = result
    else:
        display.configure(text='Undefined')
        num1 = None

    expression_display.configure(text='')
    opr = None
    new_num = True


def decimal_click():
    global new_num
    current = display.cget("text")

    if new_num or current == 'Undefined':
        display.configure(text='0.')
        new_num = False
    elif '.' not in current:
        display.configure(text=current + '.')


def clear_all():
    global num1, opr, num2, new_num

    num1 = None
    opr = None
    num2 = None
    new_num = True

    display.configure(text='0')
    expression_display.configure(text='')


# Build grid layout
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

        # Style colors per button category
        if button_text in ['+', '-', '*', '/', '=']:
            btn_color = "#1f538d"
        elif button_text == 'C':
            btn_color = "#942424"
        else:
            btn_color = "#333333"

        # Make the 'C' button fill the entire row
        col_span = 4 if button_text == 'C' else 1

        button = ctk.CTkButton(
            button_frame,
            text=button_text,
            font=('Arial', 20, 'bold'),
            width=70 if col_span == 1 else 300,
            height=55,
            fg_color=btn_color,
            command=command
        )

        button.grid(row=row, column=column, columnspan=col_span, padx=5, pady=5)

window.mainloop()