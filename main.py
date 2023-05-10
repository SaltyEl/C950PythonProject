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

setattr(truck1, 'orderedAddresses', nearestNeighbors(truck1, distanceData, addressData))
setattr(truck2, 'orderedAddresses', nearestNeighbors(truck2, distanceData, addressData))
setattr(truck3, 'orderedAddresses', nearestNeighbors(truck3, distanceData, addressData))


print(getattr(truck1, 'orderedAddresses'))
print(getattr(truck2, 'orderedAddresses'))
print(getattr(truck3, 'orderedAddresses'))

print(dt.timedelta(hours=1.9/18))

userCommand = int(input('''Please select a number from the following options: 
1. Print All Package Status and Total Mileage
2. Get a Single Package Status with a Time
3. Get All Package Status with a Time
4. Exit the Program

Enter a command (1, 2, 3, or 4): '''))

match userCommand:
    case 1:
        truck1StartTime = dt.timedelta(hours=8)
        truck2StartTime = dt.timedelta(hours=9, minutes=5)
        truck3StartTime = timeTruckIsOut(truck1) + truck1StartTime

        truck1Distance = distanceCoveredByTruck(truck1)
        truck2Distance = distanceCoveredByTruck(truck2)
        truck3Distance = distanceCoveredByTruck(truck3)

        totalDistance = truck3Distance + truck2Distance + truck1Distance

        truckDeliverPackages(truck1, truck1StartTime, packageData)
        truckDeliverPackages(truck2, truck2StartTime, packageData)
        truckDeliverPackages(truck3, truck3StartTime, packageData)

        packageData.printAll()
        print(truck3StartTime)
        print(totalDistance)


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


