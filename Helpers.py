from Loaders import *
import datetime as dt


def distBetween(distanceData, addressData, address1, address2):
    addressIndex1 = addressData.index(address1)
    addressIndex2 = addressData.index(address2)

    return float(distanceData[addressIndex1][addressIndex2])


def nearestNeighbors(truck, distances, addresses):
    address_visited = ''
    packagesToDeliver = truck.getPackagesOnTruck()
    addressDeliveryList = []
    nearestNeighborList = []

    for package in packagesToDeliver:
        address = getattr(package, 'address')
        if address not in addressDeliveryList:
            addressDeliveryList.append(address)

    while len(addressDeliveryList) > 0:
        dist_from_last = float('inf')
        for address in addressDeliveryList:
            distance = distBetween(distances, addresses, truck.location, address)
            if distance < dist_from_last:
                dist_from_last = distance
                address_visited = address
        addressDeliveryList.remove(address_visited)
        nearestNeighborList.append([address_visited, dist_from_last])
        setattr(truck, 'location', address_visited)

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
        # Use timedelta to determine how much time has passed while going from previous to current address.
        currentTime = currentTime + dt.timedelta(hours=(address[1] / 18))

        # If time checked is greater than or equal to the current
        # time during delivery, then we return the packageHashMap for
        # evaluation of packages current delivery status.
        if timeCheck is not None and timeCheck >= currentTime:
            return packageHashMap
        # If no more packages,
        if len(packageList) == 0:
            print(f'Current Address: {address[0]}')
            break
        for package in packageList:
            if package.address == address[0]:
                packageList.remove(package)
                packageHashMap.updateDeliveryStatus(package.id, True, currentTime)

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
