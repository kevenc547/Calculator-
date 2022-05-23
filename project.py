#Keven Caro,Christian Chun,Deion Stapleton

#imported libarly called tkinter
from tkinter import *
window =Tk()
window.title("Caculator ")
window.config(bg="grey")
#create a window with title called caculator with a grey background 



#create an entry box where the values could be display
#entry box is readonly the only way inporting values is by pressing the buttons 
operation=StringVar()
entry_box=Entry(window,width=35 ,readonlybackground="purple",fg="white",borderwidth=10,state="readonly",textvariable=operation)
entry_box.grid(row=0 , column=0 ,columnspan=3,padx=10, pady=10)
entry_box.focus()
#inside entry box there is varaible called  operation that will chnage values 



value= " "
#set a value where it could change in the functions and outside the fucntion 

def press(number):
    global value
    value+= str(number)
    operation.set(value)
    button_clear.config(highlightbackground="green")
    
#Function to update string of value and operation inside the enrty box
#set variable value global
#function catches  value from the butttons 
    

def button_equal():
    try:
        global value
        total=str(eval(value))
        operation.set(total)
    except:
        operation.set('error')

#fucntion evalues whats inside value 
#https://towardsdatascience.com/python-eval-built-in-function-601f87db191   
   

def button_clear():
    global value
    value=""
    operation.set("")
    button_clear.config(highlightbackground="red")
#function clears o reset the variable value


    

    


#Buttons 
#when a button is press it takes the string 
button_1=Button(window,text="1",padx=15,pady=15,command=lambda:press(1))
button_2=Button(window,text="2",padx=15,pady=15,command=lambda:press(2))
button_3=Button(window,text="3",padx=15,pady=15,command=lambda:press(3))
button_4=Button(window,text="4",padx=15,pady=15,command=lambda:press(4))
button_5=Button(window,text="5",padx=15,pady=15,command=lambda:press(5))
button_6=Button(window,text="6",padx=15,pady=15,command=lambda:press(6))
button_7=Button(window,text="7",padx=15,pady=15,command=lambda:press(7))
button_8=Button(window,text="8",padx=15,pady=15,command=lambda:press(8))
button_9=Button(window,text="9",padx=15,pady=15,command=lambda:press(9))
button_0=Button(window,text="0",padx=15,pady=15,command=lambda:press(0))
button_add=Button(window,text="+",padx=15,pady=15,highlightbackground="yellow",command=lambda: press("+"))
button_substraction =Button(window,text="-",padx=15,pady=15,highlightbackground="yellow",command=lambda:press ("-"))
button_clear=Button(window,text="clear",padx=15,pady=15,command=button_clear)
button_division=Button(window,text="/",padx=15,pady=15,highlightbackground="yellow",command=lambda:press("/"))
button_decimal=Button(window,text=".",padx=15,pady=15,command=lambda: press("."))
button_enter=Button(window,text="=",padx=15,pady=15,highlightbackground="red",command=button_equal)
button_mutliply=Button(window,text="x",padx=15,pady=15,highlightbackground="yellow",command=lambda: press("*"))
#https://www.w3schools.com/python/python_lambda.asp
#sign buttons are yellow and each time its press the equal button stays green
#when equal button is press it changes to yellow 




#buttons are placed
button_1.grid(row=3,column=0,sticky="nsew")
button_2.grid(row=3,column=1,sticky="nsew")
button_3.grid(row=3,column=2,sticky="nsew")
button_4.grid(row=2,column=0,sticky="nsew")
button_5.grid(row=2,column=1,sticky="nsew")
button_6.grid(row=2,column=2,sticky="nsew")
button_7.grid(row=1,column=0,sticky="nsew")
button_8.grid(row=1,column=1,sticky="nsew")
button_9.grid(row=1,column=2,sticky="nsew")
button_0.grid(row=4,column=0,sticky="nsew")
button_decimal.grid(row=4,column=1,sticky="nsew")
button_add.grid(row=3,column=3,sticky="nsew")
button_substraction.grid(row=4,column=3,sticky="nsew")
button_clear.grid(row=0,column=3,sticky="nsew")
button_division.grid(row=1,column=3,sticky="nsew")
button_enter.grid(row=4,column=2,sticky="nsew")
button_mutliply.grid(row=2,column=3,sticky="nsew")                                            

window.mainloop()
