# IMPORT LIBRARIES
# ==> import a relevant library in order to use the ceil function


# GLOBAL VARIABLES

nums = [15.44, 12.47, 10.16, 8.27, 10.41, 12.4, 3.47, 18.1, 7.23, 8.08, 2.34, 17.41, 3.02, 17.41, 17.37, 8.0, 19.21, 7.14, 18.85, 2.61, 16.84, 14.85, 19.02, 15.2, 9.6, 4.87, 13.85, 10.72, 0.07, 14.8, 6.93, 14.84, 7.14, 14.16, 14.98, 2.22, 6.99, 5.13, 3.41, 5.91, 7.92, 3.3, 14.69, 1.26, 15.11, 3.11, 12.91, 19.65, 9.67, 5.52, 17.22, 11.74, 14.23, 17.66, 13.68, 10.55, 2.03, 14.83, 16.66, 18.81]

startIndex = 0
endIndex = 0
ceilingTotal = 0

# MAIN PROGRAM

# input the two indexes for the totalling (inclusive)
startIndex = int(input("enter an inclusive index to start from: "))
endIndex = int(input("enter an inclusive index to end at: "))

# ==> processing loop to find total of rounded up values between these two indices


# output
print("The total of the ceiling values for list numbers in that range is {}".format(ceilingTotal))