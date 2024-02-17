#Write a program in Python to input principal amount, rate of interest and time (in years) and compute the difference between Compound Interest and Simple Interest.

#Taking Input for Principal Amount, Rate of interest and Time (in years) as P,R,T variables
p=int(input("Enter Principal Amount : ")) #Principal
r=int(input("Enter Rate : ")) #Rate
t=int(input("Enter Time (in years): ")) #Time

#Applying Formulaes for calculation
si=(p*r*t)/100 # Simple Interest = (Principal * Rate * Time) / 100
ci=p*(1+r)**t #CI = Principal * (1 + Rate of Interest)**Time

#Calculating there Difference with a new variable for clean and easy to understand progress
diff=(ci-si)

#Printing the Output
print("Difference in Compund Interest and Simple Interest is : ", diff)