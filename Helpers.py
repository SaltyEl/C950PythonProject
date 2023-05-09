from Loaders import *

def distBetween(distanceData, addressData, address1, address2):
    addressIndex1 = addressData.index(address1)
    addressIndex2 = addressData.index(address2)

    return float(distanceData[addressIndex1][addressIndex2])


'''def nearestNeighbors(truck, distances, addresses):
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
    nearestNeighborList.insert(0, ['HUB', 0.0])
    return nearestNeighborList'''

def nearestNeighbors(truck, distances, addresses):
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
    return visited_list

# def truckDeliverPackages(truck, deliveryStartTime):

