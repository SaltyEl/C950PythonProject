import sys

from Loaders import *
import datetime as dt


# This method is used to find the distance between two addresses.
# address1 and address2 are string representations of the address
# This method references the addressData in order to index the address and
# compare against the distances between them in distanceData.
def distBetween(distanceData, addressData, address1, address2):
    # Create variables to hold index of each address
    addressIndex1 = addressData.index(address1)
    addressIndex2 = addressData.index(address2)

    # Return the distance between addresses using the distance matrix provided.
    return float(distanceData[addressIndex1][addressIndex2])

# This method takes a truck object and reorders the packageList so that
# distances traveled between each address are minimized. This greedy solution
# does not guarantee an optimal solution.
def nearestNeighbors(truck, distances, addresses):
    address_visited = ''
    # Store truck package list in a variable.
    packagesToDeliver = truck.getPackagesOnTruck()
    # Create a set to hold the addresses which we need to deliver to. A set is optimal in this situation
    # as it does not allow for duplicate values (i.e. the same address twice) and sets allow for efficient
    # look up and retrieval of elements.
    addressDeliverySet = set()
    # Create a list to store the new order of the packages on the truck. This list
    # will contain nested lists, with nearestNeighborList[x][0] representing the address
    # and nearestNeighborList[x][1] representing the distance from last location.
    nearestNeighborList = []

    # For each package on the truck, add the packages associated address to the set.
    for package in packagesToDeliver:
        address = getattr(package, 'address')
        addressDeliverySet.add(address)

    # While addressDeliverySet is not empty, loop.
    while addressDeliverySet:
        # Set variable to measure initial distance against to infinity.
        dist_from_last = float('inf')
        # Iterate through each address in address set to find the next closest address to
        # trucks currents location.
        for address in addressDeliverySet:
            # Get distance between trucks current location and address in address set.
            distance = distBetween(distances, addresses, truck.location, address)
            # If distance is less than current dist_from_last, then evaluate to true.
            if distance < dist_from_last:
                # Replace dist_from_last with distance.
                dist_from_last = distance
                # Assign address to the address_visited variable.
                address_visited = address
        # Remove address_visited from addressDeliverySet, so that will not be visited more than once.
        addressDeliverySet.remove(address_visited)
        # Append list item containing address visited and the distance from previous address.
        nearestNeighborList.append([address_visited, dist_from_last])
        # Update trucks location to the current address before going through the while loop again.
        truck.location = address_visited

    # The final location visited is the HUB, so it must be added to the end of the nearestNeighborsList.
    nearestNeighborList.append(['HUB', distBetween(distances, addresses, truck.location, 'HUB')])
    # Return the nearestNeighborList to be utilized by the truckDeliverPackages function
    # and distanceCoveredByTruck function
    return nearestNeighborList


# This function takes the truck, the start time for the deliveries,
# the package data and (optionally) the time the user would like to check on the package(s) status.
# This function then delivers the packages in the designated order, and updates the delivery status
# of each package in the packageHashMap. If a timecheck is entered, the function will return the packageHashMap
# if the timecheck is less than the current time.
def truckDeliverPackages(truck, startTime, packageHashMap, timeCheck=None):
    # Create a list to store the package list containing all packages on the truck.
    packageList = truck.getPackagesOnTruck()
    # Create a list to store the addresses in the order that the truck will travel.
    orderedAddressList = truck.getOrderedAddresses()
    # Create a datetime variable that can store the start time and be updated as the truck travels.
    currentTime = startTime

    # If time is checked and is earlier than the start time, return packageHashMap without any changes.
    if timeCheck is not None and timeCheck <= startTime:
        return packageHashMap

    # Update delivery status of each package to "en route" once delivery has started.
    for package in packageList:
        packageHashMap.updateDeliveryStatus(package.id, False)

    # Deliver each package to it's address along the designated route.
    for address in orderedAddressList:
        # Create / reset a list for storing packages to be removed from truck.
        packagesToRemove = []
        # Use timedelta to determine how much time has passed while going from previous to current address.
        currentTime = currentTime + dt.timedelta(hours=(address[1] / 18))

        # If time checked is greater than or equal to the current
        # time during delivery, then we return the packageHashMap for
        # evaluation of packages current delivery status.
        if timeCheck is not None and timeCheck < currentTime:
            return packageHashMap
        # If no more packages, break the for loop. This is useful because when there
        # is one address left (the HUB), there should be no packages left. For this reason,
        # we should not need to iterate through packages further.
        if len(packageList) == 0:
            break
        # Iterate through each package in package list, and if the package matches the
        # address currently being visited, add that package to the packageToRemove list
        # and update the delivery status in the packageHashMap to delivered.
        for package in packageList:
            if package.address == address[0]:
                packagesToRemove.append(package)
                packageHashMap.updateDeliveryStatus(package.id, True, currentTime)
        # Using each package in packagesToRemove, we can delete the corresponding package in the packageList.
        for package in packagesToRemove:
            packageList.remove(package)


    return packageHashMap

# This function calculates the total distance traveled by the truck object provided
# using the nearestNeighborList (orderedAddresses) assigned to the truck.
def distanceCoveredByTruck(truck):
    totalDistance = 0
    # Use a for loop to get the sum off all address distances in list.
    for address in truck.orderedAddresses:
        totalDistance += address[1]

    return totalDistance

# This function calculates the time that the truck is out. This is useful for determining
# when trucks greater than the second truck may be able to depart (since only 2 drivers are working).
def timeTruckIsOut(truck):
    # Calculate distance covered by truck.
    distance = distanceCoveredByTruck(truck)
    # Set the trucks speed.
    truckSpeed = 18
    # Calculate the time truck is gone, and return it as timedelta.
    return dt.timedelta(hours=distance / truckSpeed)

# A function to get the time that user would like to check package(s) status.
def getUserTime():
    # Create a while loop so that if the format is wrong the user can retry, or type 'q' to quit program.
    while True:
        # Use try except block to parse out a time that has been incorrectly entered.
        try:
            # Get user time to check
            time = input("Please enter a time (HH:MM - in military format) or 'q' to quit: ")
            # Parse the user input
            if time == 'q':
                sys.exit(0)
            parsed_time = dt.datetime.strptime(time, '%H:%M')
            # Store the hours
            hours = parsed_time.hour
            # Store the minutes
            minutes = parsed_time.minute
            # Return the timedelta containing the hours and minutes of the time to be checked.
            return dt.timedelta(hours=hours, minutes=minutes)
        # Print an error to UI if time is input incorrectly
        except ValueError:
            print("This format is not exceptable.")
            continue


