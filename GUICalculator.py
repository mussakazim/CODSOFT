from tkinter import *

window = Tk()
window.geometry('500x500')
window.title('Calculator')
window.configure(bg='#3399ff')
# window.iconbitmap(path)



## ADDING FUNCTIONALITY TO THE CALCULATOR BUTTONS:
expression = ''

def press(n):
    global expression ## To access the global variable expression
    expression+=str(n)
    equation.set(expression)
    
def equal():
    try:             ## EXCEPTION HANDLING FOR ERROR (in particular division by zero)
      global expression
      total = str(eval(expression))
      equation.set(total)
      expression=''
    except:
        equation.set('Error')
        expression=''

def clear():
    global expression
    expression=''
    equation.set(expression)
 
def backspace():
    try:
      global expression
      expression = expression.rstrip(expression[-1])
      equation.set(expression)
    except:
       equation.set("Cannot Execute")
       expression = ''
    


expression_frame = Frame(window, bg='#3399ff')   ## FRAME FOR ENTRY BOX
button_frame = Frame(window,bg='#3399ff')        ## FRAME FOR BUTTONS

expression_frame.pack()
button_frame.pack()

font_entry = ('ariel', 20, 'bold')  # FOR SETTING FONT STYLE IN ENTRY BOX
font_button = ('new times roman', 15) # FOR SETTING FONT STYLE IN BUTTON
equation = StringVar()
equation.set('0')

entrybox = Entry(expression_frame, textvariable=equation, font=font_entry, justify='right')
entrybox.pack(ipadx=50,ipady=10, pady=5)
# ipadx sets vertical dimension and ipady sets horizontal dimension of box
# pady gives space between two objects in y-axis

button0 = Button(button_frame, height=3,width=5,text='0',font = font_button, relief='ridge',bg='#80bfff',borderwidth=1,command=lambda: press(0))
button1 = Button(button_frame, height=3,width=5,text='1',font = font_button, relief='ridge',bg='#80bfff',borderwidth=1,command=lambda: press(1))
button2 = Button(button_frame, height=3,width=5,text='2',font = font_button, relief='ridge',bg='#80bfff',borderwidth=1,command=lambda: press(2))
button3 = Button(button_frame, height=3,width=5,text='3',font = font_button, relief='ridge',bg='#80bfff',borderwidth=1,command=lambda: press(3))
button4 = Button(button_frame, height=3,width=5,text='4',font = font_button, relief='ridge',bg='#80bfff',borderwidth=1,command=lambda: press(4))
button5 = Button(button_frame, height=3,width=5,text='5',font = font_button, relief='ridge',bg='#80bfff',borderwidth=1,command=lambda: press(5))
button6 = Button(button_frame, height=3,width=5,text='6',font = font_button, relief='ridge',bg='#80bfff',borderwidth=1,command=lambda: press(6))
button7 = Button(button_frame, height=3,width=5,text='7',font = font_button, relief='ridge',bg='#80bfff',borderwidth=1,command=lambda: press(7))
button8 = Button(button_frame, height=3,width=5,text='8',font = font_button, relief='ridge',bg='#80bfff',borderwidth=1,command=lambda: press(8))
button9 = Button(button_frame, height=3,width=5,text='9',font = font_button, relief='ridge',bg='#80bfff',borderwidth=1,command=lambda: press(9))
buttonPlus = Button(button_frame, height=3,width=5,text='+',font = font_button, relief='ridge',bg='#80bfff',borderwidth=1,command=lambda: press('+'))
buttonMinus = Button(button_frame, height=3,width=5,text='-',font = font_button, relief='ridge',bg='#80bfff',borderwidth=1,command=lambda: press('-'))
buttonMultiply = Button(button_frame, height=3,width=5,text='*',font = font_button, relief='ridge',bg='#80bfff',borderwidth=1,command=lambda: press('*'))
buttonDivide = Button(button_frame, height=3,width=5,text='/',font = font_button, relief='ridge',bg='#80bfff',borderwidth=1,command=lambda: press('/'))
buttonEqual = Button(button_frame, height=3,width=5,text='=',font = font_button, relief='ridge',bg='#80bfff',borderwidth=1, command = equal)
buttonClear = Button(button_frame, height=3,width=5,text='C',font = font_button, relief='ridge',bg='#80bfff',borderwidth=1, command = clear)
buttonDecimal = Button(button_frame, height=3,width=5,text='.',font = font_button, relief='ridge',bg='#80bfff',borderwidth=1,command=lambda: press('.'))
buttonBack = Button(button_frame, height=3,width=5,text='<<',font = font_button, relief='ridge',bg='#80bfff',borderwidth=1, command=backspace)


button1.grid(row=0,column=0)
button2.grid(row=0,column=1)
button3.grid(row=0,column=2)
buttonPlus.grid(row=0,column=3)

button4.grid(row=1,column=0)
button5.grid(row=1,column=1)
button6.grid(row=1,column=2)
buttonMinus.grid(row=1,column=3)

button7.grid(row=2,column=0)
button8.grid(row=2,column=1)
button9.grid(row=2,column=2)
buttonMultiply.grid(row=2,column=3)

button0.grid(row=4,column=0)
buttonDecimal.grid(row=4,column=1)
buttonClear.grid(row=4,column=2)
buttonDivide.grid(row=4,column=3)

buttonEqual.grid(row=5,column=0,columnspan=3,sticky='nsew' )  ## THIS BUTTON SPANS 3 COLUMNS
buttonBack.grid(row=5,column=3)





window.mainloop()


