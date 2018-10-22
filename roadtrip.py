 # # ########################## # #
#    Multi-leg Road Trip Program   #
#         By: Nicholas Sycz        #
 # # ########################## # #

print "Calculate your Miles Per Gallon!\n"

# variable for the miles between each leg
leg1, leg2, leg3, leg4, leg5, leg6 = input("Enter the miles driven for each leg: \n")
legArray = [leg1, leg2, leg3, leg4, leg5, leg6]
miles = leg1 + leg2 + leg3 + leg4 + leg5 + leg6

print("\n")

# varaibles for the gallons used between each leg
gal1, gal2, gal3, gal4, gal5, gal6 = input("Enter the gallons used for each leg: \n")
galArray = [gal1, gal2, gal3, gal4, gal5, gal6]
gallons = gal1 + gal2 + gal3 + gal4 + gal5 + gal6

print("\n")

# individual miles per gallon of each leg

for i in range(len(legArray)):
    print "Leg", i+1,": ", legArray[i] / galArray[i],"mpg"

print "\n"

# calculation for getting the miles per gallon
mpg = miles / gallons
print "Your average fuel efficiency is: ", mpg, "mpg"


