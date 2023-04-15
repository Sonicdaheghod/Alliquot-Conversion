#Program to know how much solvent to put in fractions for tests (bioassay, LCMS, etc.)

#a- the general idea
print("""-------------- Alliquot Calculator --------------
""")

sampleMass = float(input("What is the mass of your sample in grams? "))
fractionNumber = input("What fraction is this (A,B,C, etc)?")
sampleConcentration = input("What concentration do you need to dilute your sample in? (mg/ml) ")

sampleMassmg = float(sampleMass)*1000
solventNeeded = (float(sampleMassmg)/float(sampleConcentration))*1000
# print("Sample mass in mg: ", float(sampleMassmg), "mg")
# print("Amount of solvent needed in uL: ",solventNeeded, "uL")

print("Here are the results using the provided information:\n")
print("""
| Fraction | Mass (mg) | Solvent Needed (uL) | """)

print("|   ",fractionNumber,"    | ",sampleMassmg,"  |   ",round(solventNeeded,2),"       | ")
