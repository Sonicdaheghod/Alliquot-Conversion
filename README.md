# **Alliquot-Conversion Calculator**

## **Purpose of the program**

#This program is made to assist chemists in determining the volume of the alliquot needed to plate their bioassay. The calculations saves time for them since they now will not have to do the calculations by hand and will have their results provided to them in a efficient and viewable- friendly manner. One of the challanges I faced when creating this program were including having the user to retype their input if they didn't type a numerical value. In the future, I hope to include a feature where if the user does not type a numerical value for one of the questions in the program created for a TypeError/ ValueError.

## **Example of how to use the program**

Say that a chemist knows what the mass of their crude extract is and what concentration the alliquot must be at in the well plate. They also know how many fractions they want to calculate for. So, they would type this information as shown below:

```
How many fractions do you have? 2
Enter the mass of your sample (in g): 2.3
What concentration do you need to dilute your sample in? (mg/ml) 3


```
My program will print out the mass of the extract in milligrams as well as the amount of solvent needed for based on how many fractions the user has. An example of the results from the data used above is shown here-

```
--------------Here are the results using the provided information:--------------

   Mass (mg)  Solvent Needed (ul)
0     2300.0           766.666667
1     2300.0           766.666667
Type 'continue' to use this tool again 

```
