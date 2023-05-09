from Truck import Truck
from Loaders import *
from Helpers import *
import datetime as dt

# Create a list of distance data.
distanceData = loadDistanceData("CSVFiles/DistanceFile.csv")
# Create a hashmap of package data.
packageData = loadPackageData("CSVFiles/PackageFile.csv")
# Create a list of address data.
addressData = loadAddressData("CSVFiles/DistanceFile.csv")

truck1 = Truck()
truck2 = Truck()
truck3 = Truck()

truck1.loadTruck(packageData, [1, 4, 10, 11, 13, 14, 15, 16, 17, 19, 20, 21, 22, 34, 39, 40])  # Will leave at 8:00AM.
truck2.loadTruck(packageData, [2, 3, 5, 6, 7, 8, 9, 12, 18, 25, 28, 32, 33, 36, 37, 38])  # Will leave at 9:05AM.
truck3.loadTruck(packageData, [23, 24, 26, 27, 29, 30, 31, 35])  # Will leave after first truck gets back.

setattr(truck1, 'packageList', nearestNeighbors(truck1, distanceData, addressData))
setattr(truck2, 'packageList', nearestNeighbors(truck2, distanceData, addressData))
setattr(truck3, 'packageList', nearestNeighbors(truck3, distanceData, addressData))

'''time = dt.timedelta(hours=9, minutes=5)
print(time)'''

userCommand = int(input('''Please select a number from the following options: 
1. Print All Package Status and Total Mileage
2. Get a Single Package Status with a Time
3. Get All Package Status with a Time
4. Exit the Program

Enter a command (1, 2, 3, or 4): '''))

match userCommand:
    case 1:
        print("Case 1")
    case 2:
        print("Case 2")
    case 3:
        print("Case 3")
    case 4:
        print("Case 4")
    case other:
        print("No case")

'''time = input("Please enter a time (HH:MM): ")
info = input("Single or all package tracking (Type \"Single\" or \"All\"): ")'''
'''try:
    # Parse the user input
    parsed_time = dt.datetime.strptime(time, "%I:%M")'''

