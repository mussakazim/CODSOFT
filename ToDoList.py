from tkinter import *
from tkinter.font import BOLD
from tkinter import filedialog

window = Tk()
window.geometry('700x500')
window.title('To Do List')
window.configure(bg='#43bbbf')

##Here are the Python read write methods that are most important:
# Read only r  
# Read and Write r+  (beginning of file)
# Write Only w   (over-written)
# Write and Read w+  (over written)
# Append Only a  (end of file)
# Append and Read a+  (end of file)


def createnew():
    createwindow = Toplevel()  ## TopLevel() function creates a new window
    createwindow.title('Create List')
    createwindow.geometry('700x500')
    createwindow.configure(bg='#43bbbf')
    def save1():
      name = listname.get(1.0,END)
      ## name=name.strip(name[-1])
      name=name.replace('\n','')
      file = open(f"To Do Lists\\{name}.txt","w")
      file.write(contentbox.get(1.0,END))##TEXT BOXES START AT INDEX 1.0
      file.close()
      createwindow.destroy()
   
    text1 = Label(createwindow, width=50,height=3,text = "List Name:", relief='flat',bg ='#43bbbf',font=('new times roman',14, BOLD))
    text1.pack(pady=3)
    
    listname = Text(createwindow,width=10,height=0.1, font=('new times roman',12))
    listname.pack(ipadx=50,pady=1)
    
    text2 = Label(createwindow, width=50,height=3,text = "List Content:", relief='flat',bg ='#43bbbf',font=('new times roman',14, BOLD))
    text2.pack(pady=3)
    contentbox = Text(createwindow,width=50,height=10,font=('ariel',12))
    contentbox.pack()
    
    save1button = Button(createwindow,width=8,height=2,text='Save', relief='raised',bg='#c91c30',font=('new times roman',14,BOLD),command=save1)
    #command=createwindow.destroy  --> to close the box
    save1button.pack(pady=8)


def updatelist():
   createwindow = Toplevel()  ## TopLevel() function creates a new window
   createwindow.title('Update List')
   createwindow.geometry('700x500')
   createwindow.configure(bg='#43bbbf')

   def openfile():
      file1 = filedialog.askopenfilename(initialdir="To Do Lists\\",title="Open Lists", filetypes=(("Text Files","*.txt"),))
      fileopen = open(file1,'r')
      read = fileopen.read()
      
      contentbox2.insert(END,read)
      fileopen.close() 
      
      def save2():
         fileopen = open(file1,'w')
         fileopen.write(contentbox2.get(1.0,END))
         fileopen.close()
         
         createwindow.destroy()
      
      buttonSave = Button(createwindow, width=20,height=3,text = "SAVE", relief='raised',bg ='#c91c30',font=('new times roman',12, BOLD),command=save2)
      buttonSave.pack(pady=10)
      
      
                  
   buttonChoose = Button(createwindow, width=20,height=3,text = "Choose List", relief='raised',bg ='#c91c30',font=('new times roman',12, BOLD),command=openfile)
   buttonChoose.pack(pady=10)   

   contentbox2 = Text(createwindow,width=50,height=10,font=('ariel',12))
   contentbox2.pack(pady=5)
   
   
   
def viewlists():
   createwindow = Toplevel()  ## TopLevel() function creates a new window
   createwindow.title('View List')
   createwindow.geometry('700x500')
   createwindow.configure(bg='#43bbbf')
   
   def openfile():
      file1 = filedialog.askopenfilename(initialdir="To Do Lists\\",title="Open Lists", filetypes=(("Text Files","*.txt"),))
      fileopen = open(file1,'r')
      read = fileopen.read()
      
      contentbox3.insert(END,read)
      fileopen.close()
   
   buttonChoose = Button(createwindow, width=20,height=3,text = "Choose List", relief='raised',bg ='#c91c30',font=('new times roman',12, BOLD),command=openfile)
   buttonChoose.pack(pady=10)  
   
   contentbox3 = Text(createwindow,width=50,height=15,font=('ariel',12))
   contentbox3.pack(pady=5)
   
   buttonExit =  Button(createwindow, width=10,height=3,text = "EXIT",foreground='white', relief='raised',bg ='#0d0d0d',font=('new times roman',12, BOLD),command=createwindow.destroy)
   buttonExit.pack(pady=5)
   

   


    

    


title_frame = Frame(window, bg='#43bbbf')
title_frame.pack()
button_frame=Frame(window, bg='#43bbbf')
button_frame.pack()

heading = Label(title_frame, width=50,height=3,text = "TO DO LIST", relief='flat',bg ='#413ac2',font=('new times roman',20, BOLD))
heading.pack(pady=5,fill=X)

buttonCreate = Button(button_frame, width=10,height=3,text = "Create", relief='raised',bg ='#c91c30',font=('new times roman',12, BOLD),command=createnew)
buttonUpdate= Button(button_frame, width=20,height=3,text = "Update", relief='raised',bg ='#c91c30',font=('new times roman',12, BOLD),command=updatelist)
buttonView= Button(button_frame, width=20,height=3,text = "View", relief='raised',bg ='#c91c30',font=('new times roman',12, BOLD),command=viewlists)
buttonExit= Button(button_frame, width=10,height=3,text = "EXIT",foreground='white', relief='raised',bg ='#0d0d0d',font=('new times roman',12, BOLD),command=window.destroy)

buttonCreate.pack(pady=5)
buttonUpdate.pack(pady=5)
buttonView.pack(pady=5)
buttonExit.pack(pady=5)


window.mainloop()
