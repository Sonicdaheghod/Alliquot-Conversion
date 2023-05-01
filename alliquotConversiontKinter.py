#credit to https://python-course.eu/tkinter/entry-widgets-in-tkinter.php for help with input text boxes

# #1 - bring in tKinter application window
import tkinter as tk


appWindow = tk.Tk()
appWindow.title("Aliquot Calculator")

#2 - Adding inputs for user

# ##labels for input
tk.Label(appWindow, text="Mass of sample (mg)").grid(row=0)
tk.Label(appWindow, text="Concentration needed (mg/uL)").grid(row=1)

e1 = tk.Entry(appWindow)
e2 = tk.Entry(appWindow)

##text box for inputs

e1.grid(row=0, column=1)
e2.grid(row=1, column=1)

appWindow.mainloop()
