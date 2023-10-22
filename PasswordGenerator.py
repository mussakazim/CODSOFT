from tkinter import *
import random
from tracemalloc import start

window = Tk()
window.geometry('500x500')
window.title('Password Generator')
window.configure(bg='#ffffff')

uppercase = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
lowercase = uppercase.lower()
digits = '0123456789'

all = ''
all = all + uppercase + lowercase + digits

def generate():
    password = ''
    buttonans.delete(1.0,'end')
    try:
        global all
        length = buttonlen.get('1.0','end-1c') ## From starting to end by just eliminating the last char that text box produces itself
        length = int(length)
    
        for x in range(1):
            password = "".join(random.sample(all,length))
        buttonans.insert(END, password)
    except:
       buttonans.insert(END,'ERROR')
    
heading = Label(window, width=50,height=3,text = "Password Generator", relief='flat',bg ='#87CEEB',font=('new times roman',20))
heading.pack(pady=5,fill=X)

text2 = Label(window, width=50,height=3,text = "Enter desired length of password:", relief='flat',bg ='#ffffff',font=('new times roman',10))
text2.pack(pady=1)

buttonlen = Text(window,width=20,height=1, font=('ariel',12))
buttonlen.pack(pady=3)

button0 = Button(window, height=5,width=15,text='Generate',relief='ridge',bg='#80bfff',borderwidth=1,command=generate)
button0.pack(pady=10)

buttonans = Text(window,height=1,width=50,font=('ariel',12))
buttonans.pack(pady=10)

buttonExit =  Button(window, width=7,height=2,text = "EXIT",foreground='white', relief='raised',bg ='#0d0d0d',font=('new times roman',12),command=window.destroy)
buttonExit.pack(pady=15)

window.mainloop()
