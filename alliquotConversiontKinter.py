#credit to https://python-course.eu/tkinter/entry-widgets-in-tkinter.php for help with input text boxes

import tkinter as tk

#1 - user entries
userInputs = ("Mass of sample (mg)","Concentration of aliquot (mg/ml)")

#2- making boxes and functionality for user inputs
def solventNeeded(enteries):
    solvent = ((float(enteries["Mass of sample (mg)"].get()))/(float(enteries["Concentration of aliquot (mg/ml)"].get()))*1000)
    print("Solvent needed (uL): ", solvent)

 
def makeform(root, userInputs):
    entries = {}
    for field in userInputs:
        print(field)
        row = tk.Frame(root)
        lab = tk.Label(row, width=35, text=field+": ", anchor='w')
        ent = tk.Entry(row)
        ent.insert(0, "0")
        row.pack(side=tk.TOP, 
                 fill=tk.X, 
                 padx=15, 
                 pady=15)
        lab.pack(side=tk.LEFT)
        ent.pack(side=tk.RIGHT, 
                 expand=tk.YES, 
                 fill=tk.X)
        entries[field] = ent
    return entries

#3 - forming the tkinter application and output button
if __name__ == '__main__':
    root = tk.Tk()
    root.title("Aliquot Calculator")
    ents = makeform(root, userInputs)
    b1 = tk.Button(root, text='Final Calculation',
           command=(lambda e=ents: solventNeeded(e)))
    b1.pack(side=tk.LEFT, padx=5, pady=5)

    root.mainloop()

