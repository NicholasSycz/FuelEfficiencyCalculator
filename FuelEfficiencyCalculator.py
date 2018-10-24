 # # ########################### # #
#    Multi-leg Road Trip Program    #
#        By: Nicholas Sycz          #
 # # ########################### # #
import csv
import sys

print "Calculating your Miles Per Gallon!\n"

# Reading the file
rt       = open(raw_input("enter a file: "))
csv_fil  = csv.reader(rt)

# Array variables to store the data in the file
dist = []
gal = []

# Looping through the csv file and putting row values into separate arrays
for row in csv_fil:
    dist.append(int(row[0]))
    gal.append(int(row[1]))

# Looping through the arrays to calculate mpg
for i in range(len(dist)):
    mpg = dist[i] / gal[i]
    print "Leg",i+1,": ", mpg

print "Your average fuel efficiency is: ",mpg,"mpg"
