#import all necessary libraries
from tkinter import *
import tkinter.messagebox

tk = Tk()
#assigning a title
tk.title("Tic Tac Toe")

#assigning a variable click to the condition true
click=True

'''
checks the button's status
parameter passed:
buttons(string)
'''
def check(buttons):
	#assign click as a global variable
	global click

	#if button is empty and clicked, print X
	if buttons["text"]==" " and click==True:
		buttons["text"]= "X"
		click=False

	#if button is empty and it gets clicked, print O
	elif buttons["text"]==" " and click==False:
		buttons["text"]="O"
		click=True

	#if buttons 1,2,3 contain X, print X as winner 
	if(button1["text"]=="X" and button2["text"]=="X" and button3["text"]=="X"):
		tkinter.messagebox.showinfo("Winner X", "Congratulations you won")

	#if buttons 4,5,6 contain X, print X as winner 
	if(button4["text"]=="X" and button5["text"]=="X" and button6["text"]=="X"):
		tkinter.messagebox.showinfo("Winner X", "Congratulations you won")

	#if buttons 7,8,9 contain X, print X as winner
	if(button7["text"]=="X" and button8["text"]=="X" and button9["text"]=="X"):
		tkinter.messagebox.showinfo("Winner X", "Congratulations you won")

	#if buttons 3,5,7 contain X, print X as winner
	if(button3["text"]=="X" and button5["text"]=="X" and button7["text"]=="X"):
		tkinter.messagebox.showinfo("Winner X", "Congratulations you won")

	#if buttons 1,5,9 contain X, print X as winner
	if(button1["text"]=="X" and button5["text"]=="X" and button9["text"]=="X"):
		tkinter.messagebox.showinfo("Winner X", "Congratulations you won")

	#if buttons 1,4,7 contain X, print X as winner
	if(button1["text"]=="X" and button4["text"]=="X" and button7["text"]=="X"):
		tkinter.messagebox.showinfo("Winner X", "Congratulations you won")

	#if buttons 2,5,8 contain X, print X as winner
	if(button2["text"]=="X" and button5["text"]=="X" and button8["text"]=="X"):
		tkinter.messagebox.showinfo("Winner X", "Congratulations you won")

	#if buttons 3,6,9 contain X, print X as winner
	if(button3["text"]=="X" and button6["text"]=="X" and button9["text"]=="X"):
		tkinter.messagebox.showinfo("Winner X", "Congratulations you won")

	#if buttons 1,2,3 contain O, print O as winner
	if(button1["text"]=="O" and button2["text"]=="O" and button3["text"]=="O"):
		tkinter.messagebox.showinfo("Winner O", "Congratulations you won")

	#if buttons 4,5,6 contain O, print O as winner
	if(button4["text"]=="O" and button5["text"]=="O" and button6["text"]=="O"):
		tkinter.messagebox.showinfo("Winner O", "Congratulations you won")

	#if buttons 7,8,9 contain O, print O as winner
	if(button7["text"]=="O" and button8["text"]=="O" and button9["text"]=="O"):
		tkinter.messagebox.showinfo("Winner O", "Congratulations you won")

	#if buttons 3,5,7 contain O, print O as winner
	if(button3["text"]=="O" and button5["text"]=="O" and button7["text"]=="O"):
		tkinter.messagebox.showinfo("Winner O", "Congratulations you won")

	#if buttons 1,5,9 contain O, print O as winner
	if(button1["text"]=="O" and button5["text"]=="O" and button9["text"]=="O"):
		tkinter.messagebox.showinfo("Winner O", "Congratulations you won")

	#if buttons 1,4,7 contain O, print O as winner
	if(button1["text"]=="O" and button4["text"]=="O" and button7["text"]=="O"):
		tkinter.messagebox.showinfo("Winner O", "Congratulations you won")

	#if buttons 2,5,8 contain O, print O as winner
	if(button2["text"]=="O" and button5["text"]=="O" and button8["text"]=="O"):
		tkinter.messagebox.showinfo("Winner O", "Congratulations you won")

	#if buttons 3,6,9 contain O, print O as winner
	if(button3["text"]=="O" and button6["text"]=="O" and button9["text"]=="O"):
		tkinter.messagebox.showinfo("Winner O", "Congratulations you won")

	#if the complete grid is empty, pass
	if button1 == ' ' or button2 == ' ' or button3 == ' ' or button4 == ' ' or button5 == ' ' or button6 == ' ' or button7 == ' ' or button8 == ' ' or button9 == ' ':
		pass

	#if all the above conditions are false, print no one won
	# else:
	# 	tkinter.messagebox.showinfo("No one won")

'''
construct a function to clear the grid
parameters passed:
buttons(string)
'''

#function to clear the grid
def clear_all():
	button1['text']=' '
	button2['text']=' '
	button3['text']=' '
	button4['text']=' '
	button5['text']=' '
	button6['text']=' '
	button7['text']=' '
	button8['text']=' '
	button9['text']=' '



#the variable buttons is of the type string
buttons=StringVar()

'''
button specifications:
text,font,size and placing of a button in the form of a grid
'''
#button specifications
button1=Button(tk,text=" ",font=('Times 26 bold'),height=4,width=8,command=lambda:check(button1))
button1.grid(row=0,column=0,sticky=S+N+E+W)

button2=Button(tk,text=" ",font=('Times 26 bold'),height=4,width=8,command=lambda:check(button2))
button2.grid(row=0,column=1,sticky=S+N+E+W)

button3=Button(tk,text=" ",font=('Times 26 bold'),height=4,width=8,command=lambda:check(button3))
button3.grid(row=0,column=2,sticky=S+N+E+W)

button4=Button(tk,text=" ",font=('Times 26 bold'),height=4,width=8,command=lambda:check(button4))
button4.grid(row=1,column=0,sticky=S+N+E+W)

button5=Button(tk,text=" ",font=('Times 26 bold'),height=4,width=8,command=lambda:check(button5))
button5.grid(row=1,column=1,sticky=S+N+E+W)

button6=Button(tk,text=" ",font=('Times 26 bold'),height=4,width=8,command=lambda:check(button6))
button6.grid(row=1,column=2,sticky=S+N+E+W)

button7=Button(tk,text=" ",font=('Times 26 bold'),height=4,width=8,command=lambda:check(button7))
button7.grid(row=2,column=0,sticky=S+N+E+W)

button8=Button(tk,text=" ",font=('Times 26 bold'),height=4,width=8,command=lambda:check(button8))
button8.grid(row=2,column=1,sticky=S+N+E+W)

button9=Button(tk,text=" ",font=('Times 26 bold'),height=4,width=8,command=lambda:check(button9))
button9.grid(row=2,column=2,sticky=S+N+E+W)

button10=Button(tk,text="Clear",font=('Times 26 bold'),command=clear_all)
button10.grid(row=3,column=1,sticky=E+W)


tk.mainloop()