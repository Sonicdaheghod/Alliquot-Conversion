#Program to know how much solvent to put in fractions for tests (bioassay, LCMS, etc.)
#This program is specific for my bioassay preperation for my fungal samples I am working on for my honors thesis research project on reisolating metabolites

import pandas as pd
while True:
    print("""-------------- Alliquot Calculator --------------
    """)

    #input only accepts number inputs
    try:
        fractionNumber = int(input("How many fractions do you have? "))
        
    except ValueError:
        print("Invalid response. Type in a number.")
        continue
        
    sampleMass = []
    solventNeeded = []


    for i in range(fractionNumber):
      
        #print mass in mg
        sampleMassInput = float(input("Enter the mass of your sample (in g): "))

       
        
        calculationMass = float(sampleMassInput)*1000
        sampleMass.append(calculationMass)
        #use concentration to print out desired amoutn solvent
        sampleConcentrationInput = input("What concentration do you need to dilute your sample in? (mg/ml) ")


        calculationConcentrationInput = float((float(sampleMassInput)/float(sampleConcentrationInput))*1000)
        solventNeeded.append(calculationConcentrationInput)


    labelTable = {'Mass (mg)':sampleMass,'Solvent Needed (ul)':solventNeeded}
    makeTable = pd.DataFrame(labelTable)
    #output table
    print("\n")
    print("--------------Here are the results using the provided information:--------------\n")
    print(makeTable)

    #need to loop program
    askInput = input("""Type 'continue' to use this tool again """)
    if askInput == "continue" or "Continue":
        continue
    else:
        break
