from tkinter import *

def button_press(number) :
    global operation_text

    operation_text= operation_text + str(num)
    operation_label.set(operation_text)
def equals() :
    pass

def clear() : 
    pass

window=Tk() #creating the whole window, without the * in import we write window=tk.Tk()
window.configure(bg='beige') #its optional for window configuration

#now lets start customizing it :

window.title("my calculator")
window.geometry("650x600") #setting the window dimensions

operation_text="" #we created a string variable where we gonna write the operation every press of button
operation_label=StringVar() #stringvar is a class constructor belongs to tkinter that creates a variable that can hold a string value to sync (or connect) with tkinter widgets like buttons labels and entries
my_label=Label(window, textvariable=operation_label, font=('stylish', 22), bg="purple", width=22, height=2)

my_label.pack(pady=50) #display the label on the screen (its usual written .pack() but for positionning configuration we added pady to make it a little bit lower))
frame= Frame(window,bg='purple') # we created a frame where we gonna put the buttons in to look better, we created it using the frame constructor Frame()
frame.pack(padx=(10,100)) #to show the frame, we added anchor and padx to move the frame because its in the middle by default pack()
button1=Button(frame,font=('arial',35),height=1,width=2,text=1,fg='beige',bg='purple',
 command= lambda: button_press(1)) #button() make a clickable button object, command define how the button reacts to the click : it should pass 1 to button_press function
button1.grid(row=0,column=0) # this so important for positioning the button, without it the button would not be even shown 

button2=Button(frame,font=('arial',35),height=1,width=2,text=2,fg='beige',bg='purple', command= lambda: button_press(2))
button2.grid(row=0,column=1)

button3=Button(frame,font=('arial',35),height=1,width=2,text=3,fg='beige',bg='purple', command= lambda: button_press(3))
button3.grid(row=0,column=2)

button4=Button(frame,font=('arial',35),height=1,width=2,text=4,fg='beige',bg='purple', command= lambda: button_press(4))
button4.grid(row=1,column=0)

button5=Button(frame,font=('arial',35),height=1,width=2,text=5,fg='beige',bg='purple', command= lambda: button_press(5))
button5.grid(row=1,column=1)

button6=Button(frame,font=('arial',35),height=1,width=2,text=6,fg='beige',bg='purple', command= lambda: button_press(6))
button6.grid(row=1,column=2)

button7=Button(frame,font=('arial',35),height=1,width=2,text=7,fg='beige',bg='purple', command= lambda: button_press(7))
button7.grid(row=2,column=0)

button8=Button(frame,font=('arial',35),height=1,width=2,text=8,fg='beige',bg='purple', command= lambda: button_press(8))
button8.grid(row=2,column=1)

button9=Button(frame,font=('arial',35),height=1,width=2,text=9,fg='beige',bg='purple', command= lambda: button_press(9))
button9.grid(row=2,column=2)


button0=Button(frame,font=('arial',35),height=1,width=2,text=0,fg='beige',bg='purple', command= lambda: button_press(0))
button0.grid(row=0,column=3)

buttonmult=Button(frame,font=('arial',35),height=1,width=2,text='*',fg='beige',bg='purple', command= lambda: button_press('*'))
buttonmult.grid(row=0,column=4)

buttonplus=Button(frame,font=('arial',35),height=1,width=2,text='+',fg='beige',bg='purple', command= lambda: button_press('+'))
buttonplus.grid(row=1,column=3)

buttonminus=Button(frame,font=('arial',35),height=1,width=2,text='-',fg='beige',bg='purple', command= lambda: button_press('-'))
buttonminus.grid(row=1,column=4)

buttondivide=Button(frame,font=('arial',35),height=1,width=2,text='/',fg='beige',bg='purple', command= lambda: button_press('/'))
buttondivide.grid(row=2,column=3)

buttonpower=Button(frame,font=('arial',35),height=1,width=2,text='**',fg='beige',bg='purple', command= lambda: button_press('**'))
buttonpower.grid(row=2,column=4)

clearbutton = Button(window, text='clear', height=4, width=8, font=35,bg='purple',fg='beige', command=lambda : clear())
clearbutton.pack()

buttonequal=Button(frame,font=('arial',35),height=1,width=10,text='=',fg='beige',bg='purple', command= lambda: equals())
buttonequal.grid(row=4, column=4)

window.mainloop()