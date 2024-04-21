from tkinter import *
import math as m




root = Tk() # creating the window


root.title("B Calculator")  # to set the tittle of our window

root.config(bg="dodgerblue") # to set the background colour of my calculator

root.geometry("350x380") # to set the Width and the height

entry = Entry(root, font=("times new roman", 20, "bold"), bg="black", fg="white", 
              bd=10, relief=SUNKEN, width=30) 
entry.grid(row=0, column=0,columnspan=8)# the entry creates the frame where the numbers will be displayed

button_text_list = ["C", "CE", "√", "+", "π", "cos", "tan", "sin", "^",
              "1", "2", "3", "-", "2π", "cosh", "tanh", "sinh",
              "4", "5", "6", "+", chr(8731),"In", "deg", "rad", "=", "*",
              "7", "8", "9",chr(247), "%", "0", ".", "/", "(", ")", "e", "x!", "log10"]
rowvalue =1
columnvalue = 0

for i in button_text_list:# use a for loop to access the buttons
    button = Button(root, width=5, height=2, relief=SUNKEN, text=i, bg="cadetblue", fg="white" ,font=("times new roman", 20, "bold"),
                    activebackground="cadetblue", command=lambda button=i:click(button))
    button.grid(row=rowvalue, column=columnvalue, pady=1,padx=5 )# to create button for the calculator
    # to add one to the number of the button starting from the second one
    columnvalue += 1
    if columnvalue > 7:
        rowvalue += 1
        columnvalue = 0

def click(value):
    # print(value)
    ac = entry.get()
    answer =" "
    
    # use if statement to access the buttons so it can be usable
    # it is used incase if there is any error
    try:
        if value == "C":
            ac=ac [0:len(ac)-1]
            entry.delete(0, END)
            entry.insert(0, ac)
            
        elif value == "CE":
            entry.delete(0, END)
            
        elif value == "√":
            answer =m.sqrt(eval(ac))
        
        
        elif value == "π":
            answer =m.pi
            
        elif value == "cos":
            answer =m.cos(m.radians(eval(ac)))
        
        elif value == "tan":
            answer =m.tan(m.radians(eval(ac)))
            
        elif value == "sin":
            answer =m.sin(m.radians(eval(ac)))
        
        elif value == "2π":
            answer =2*m.pi
            
        elif value == "cosh":
            answer = m.cosh(eval(ac))
        
        elif value == "tanh":
            answer = m.tanh(eval(ac))
        
        elif value == "sinh":
            answer = m.sinh(eval(ac))
            
        elif value == "^":
            answer =eval(ac)*2
        
        
        elif value == chr(8731):
            answer =eval(ac)**(1/3)
        
        elif value == "In":
            answer =m.log2(eval(ac))
        
        elif value == "deg":
            answer =m.degrees(eval(ac))
            
        
        elif value == "rad":
            answer = m.radians(eval(ac))
            
        elif value == "e":
            answer = m.e
        
        elif value == "log":
            answer = m.log10(eval(ac))
            
        elif value == "x!":
            answer = m.factorial(eval(ac))
        
        elif value == chr(247):
            entry.insert(END, "/")
            return
        
        elif value == "=":
            answer = eval(ac)    
            
        else:
            entry.insert(END, value)
            return
        
    
        entry.delete(0, END)
        entry.insert(0, answer)
    
    
    except SyntaxError:
        pass    
        


# this is used so the code can be able to run
root.mainloop()

