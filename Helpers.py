import sys

from Loaders import *
import datetime as dt


def distBetween(distanceData, addressData, address1, address2):
    addressIndex1 = addressData.index(address1)
    addressIndex2 = addressData.index(address2)

    return float(distanceData[addressIndex1][addressIndex2])


def nearestNeighbors(truck, distances, addresses):
    address_visited = ''
    packagesToDeliver = truck.getPackagesOnTruck()
    addressDeliverySet = set()
    nearestNeighborList = []

    for package in packagesToDeliver:
        address = getattr(package, 'address')
        addressDeliverySet.add(address)

    while addressDeliverySet:
        dist_from_last = float('inf')
        for address in addressDeliverySet:
            distance = distBetween(distances, addresses, truck.location, address)
            if distance < dist_from_last:
                dist_from_last = distance
                address_visited = address
        addressDeliverySet.remove(address_visited)
        nearestNeighborList.append([address_visited, dist_from_last])
        truck.location = address_visited

    nearestNeighborList.append(['HUB', distBetween(distances, addresses, truck.location, 'HUB')])
    return nearestNeighborList


'''def nearestNeighbors(truck, distances, addresses):
    address_visited = ''
    packagesToDeliver = truck.getPackagesOnTruck()
    addressDeliveryList = []
    visited_list = []

    for package in packagesToDeliver:
        address = getattr(package, 'address')
        if address not in addressDeliveryList:
            addressDeliveryList.append(address)

    while len(visited_list) < len(addressDeliveryList):
        min_dist = float('inf')
        for address in addressDeliveryList:
            distance = distBetween(distances, addresses, truck.location, address)
            if distance < min_dist and address not in visited_list:
                min_dist = distance
                address_visited = address
        visited_list.append(address_visited)
        setattr(truck, 'location', address_visited)

    visited_list.append('HUB')
    return visited_list'''


def truckDeliverPackages(truck, startTime, packageHashMap, timeCheck=None):
    packageList = truck.getPackagesOnTruck()
    orderedAddressList = truck.getAddressList()
    currentTime = startTime

    # If time is checked and is earlier than the start time, return packageHashMap without any changes.
    if timeCheck is not None and timeCheck <= startTime:
        return packageHashMap

    # Update delivery status of each package to "en route" once delivery has started.
    for package in packageList:
        id = package.id
        packageHashMap.updateDeliveryStatus(id, False)

    # Deliver each package to it's address along the designated route.
    for address in orderedAddressList:
        packagesToRemove = []
        # Use timedelta to determine how much time has passed while going from previous to current address.
        currentTime = currentTime + dt.timedelta(hours=(address[1] / 18))

        # If time checked is greater than or equal to the current
        # time during delivery, then we return the packageHashMap for
        # evaluation of packages current delivery status.
        if timeCheck is not None and timeCheck < currentTime:
            print(f'Operation exited at {currentTime}')
            return packageHashMap
        # If no more packages,
        if len(packageList) == 0:
            break
        for package in packageList:
            if package.address == address[0]:
                packagesToRemove.append(package)
                packageHashMap.updateDeliveryStatus(package.id, True, currentTime)

        for package in packagesToRemove:
            packageList.remove(package)


    return packageHashMap

def distanceCoveredByTruck(truck):
    totalDistance = 0

    for address in truck.orderedAddresses:
        totalDistance += address[1]

    return totalDistance

def timeTruckIsOut(truck):
    distance = distanceCoveredByTruck(truck)
    truckSpeed = 18
    return dt.timedelta(hours=distance / truckSpeed)

# A function to get the time that user would like to check package(s) status.
def getUserTime():
    # Create a while loop so that if the format is wrong the user can retry, or type 'q' to quit program.
    while True:
        # Use try except block to parse out a time that has been incorrectly entered.
        try:
            # Get user time to check
            time = input("Please enter a time (HH:MM) or 'q' to quit: ")
            # Parse the user input
            if time == 'q':
                sys.exit(0)
            parsed_time = dt.datetime.strptime(time, '%I:%M')
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


