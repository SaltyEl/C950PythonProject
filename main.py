# Name: Blake Ramsey. Student ID: 000425505

import Helpers
from Truck import Truck
from Helpers import *
import datetime as dt

# Create a list of distance data.
distanceData = loadDistanceData("CSVFiles/DistanceFile.csv")
# Create a hashmap of package data.
packageData = loadPackageData("CSVFiles/PackageFile.csv")
# Create a list of address data.
addressData = loadAddressData("CSVFiles/DistanceFile.csv")

# Create 3 instances of Truck
truck1 = Truck("Truck 1")
truck2 = Truck("Truck 2")
truck3 = Truck("Truck 3")

# Manually load packages onto each truck, while not exceeding truck package limit.
truck1.loadTruck(packageData, [8, 11, 13, 14, 15, 16, 17, 19, 20, 21, 22, 30, 34, 37, 39, 40])  # Will leave at 8:00AM.
truck2.loadTruck(packageData, [1, 3, 5, 6, 7, 12, 18, 25, 28, 29, 31, 32, 36, 38])  # Will leave at 9:05AM.
truck3.loadTruck(packageData, [10, 2, 4, 9, 23, 24, 26, 27, 33, 35])  # Will leave after first truck gets back.

# Assign each package on the truck to the truck.
truck1.assignPackagesToTruck(packageData)
truck2.assignPackagesToTruck(packageData)
truck3.assignPackagesToTruck(packageData)

# Set the order that trucks will travel to each address using nearestNeighbors algorithm.
truck1.orderedAddresses = nearestNeighbors(truck1, distanceData, addressData)
truck2.orderedAddresses = nearestNeighbors(truck2, distanceData, addressData)
truck3.orderedAddresses = nearestNeighbors(truck3, distanceData, addressData)

# Set truck start times.
truck1StartTime = dt.timedelta(hours=8)
truck2StartTime = dt.timedelta(hours=9, minutes=5)
truck3StartTime = timeTruckIsOut(truck1) + truck1StartTime

# Repeat match case until appropriate response is given by user.
while True:
    # Prompt user for input.
    userCommand = int(input('''Please select a number from the following options: 
    1. Print All Package Status and Total Mileage
    2. Get a Single Package Status with a Time
    3. Get All Package Status with a Time
    4. Exit the Program

    Enter a command (1, 2, 3, or 4): '''))
    # Use match case to provide user with desired information of packages / delivery.
    match userCommand:
        case 1:
            # Get distances covered by each truck during delivery.
            truck1Distance = distanceCoveredByTruck(truck1)
            truck2Distance = distanceCoveredByTruck(truck2)
            truck3Distance = distanceCoveredByTruck(truck3)

            # Store total distance covered by all trucks in a variable to present to user.
            totalDistance = truck3Distance + truck2Distance + truck1Distance

            # Deliver the packages without a time constraint.
            truckDeliverPackages(truck1, truck1StartTime, packageData)
            truckDeliverPackages(truck2, truck2StartTime, packageData)
            truckDeliverPackages(truck3, truck3StartTime, packageData)

            # Format total distance to be presented to user.
            format_distance = "{:.2f}".format(totalDistance)
            # Print total distance to user interface.
            print(f'The total mileage traveled for all trucks is {format_distance} miles')
            # Print all package information after trucks have run their routes.
            packageData.printAll()
            break

        case 2:
            # Get time at which user would like to check package delivery status.
            timeCheck = Helpers.getUserTime()
            # Get ID of package and store in a variable
            key = int(input("Please enter package ID: "))

            # Deliver the packages with a time constraint.
            truckDeliverPackages(truck1, truck1StartTime, packageData, timeCheck)
            truckDeliverPackages(truck2, truck2StartTime, packageData, timeCheck)
            truckDeliverPackages(truck3, truck3StartTime, packageData, timeCheck)

            # Store package information in a package variable.
            package = packageData.get(key)
            # Print package status information for user.
            print(package)
            break

        case 3:
            # Get time at which user would like to check package delivery status.
            timeCheck = Helpers.getUserTime()

            # Deliver the packages with a time constraint.
            truckDeliverPackages(truck1, truck1StartTime, packageData, timeCheck)
            truckDeliverPackages(truck2, truck2StartTime, packageData, timeCheck)
            truckDeliverPackages(truck3, truck3StartTime, packageData, timeCheck)

            # Print all package status information for user.
            packageData.printAll()
            break
        case 4:
            print("Goodbye!")
            # Exit program.
            sys.exit(0)
        case other:
            print("Please select from commands provided.")
            continue
