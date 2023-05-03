#credit to https://python-course.eu/tkinter/entry-widgets-in-tkinter.php for help with input text boxes

import tkinter as tk

#user entries
userInputs = ("Mass of sample (mg)","Concentration of aliquot (mg/ml)")

def solventNeeded(enteries):
    solvent = ((float(enteries["Mass of sample (mg)"].get()))/(float(enteries["Concentration of aliquot (mg/ml)"].get()))*1000)
    print("Solvent needed (uL): ", solvent)

def makeform(root, userInputs):
    entries = {}
    for field in userInputs:
        print(field)
        row = tk.Frame(root)
        label = tk.Label(row, width=35, text=field+": ", anchor='w')
        entry = tk.Entry(row)
        entry.insert(0, "0")
        row.pack(side=tk.TOP, 
                 fill=tk.X, 
                 padx=15, 
                 pady=15)
        label.pack(side=tk.LEFT)
        entry.pack(side=tk.RIGHT, 
                 expand=tk.YES, 
                 fill=tk.X)
        entries[field] = entry
    return entries

if __name__ == '__main__':
    appRoot = tk.Tk()
    appRoot.title("Aliquot Calculator")
    ents = makeform(appRoot, userInputs)
    b1 = tk.Button(appRoot, text='Final Calculation',
           command=(lambda e=ents: solventNeeded(e)))
    b1.pack(side=tk.LEFT, padx=5, pady=5)

    appRoot.mainloop()

