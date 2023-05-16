import csv
from Package import Package
from PackageHashMap import PackageHashMap

# This function takes a csv file and reads the data, converting it into a matrix that can be accessed to
# find distances between two locations. The csv file used is only half complete, so an algorithm is used
# to complete the matrix.
def loadDistanceData(fileName):
    distanceLists = []

    # Read the information from the distance csv into a matrix.
    with open(fileName) as distanceFile:
        distanceData = csv.reader(distanceFile, delimiter=',')
        # For each row, append the distances from that row into the distanceList matrix.
        for row in distanceData:
            distanceList = []
            for i in range(1, 28):
                distanceList.append(row[i])

            distanceLists.append(distanceList)
    # Below is an algorithm that iterates through the empty cells in the matrix, and fills
    # them with the inverse value. This works because the distance between address A and address B
    # is the same, regardless of which address is the start point.
    end_column = 0
    for row in range(len(distanceLists)):
        column = 26
        while column != end_column:
            distanceLists[row][column] = distanceLists[column][row]
            column -= 1
        end_column += 1

    return distanceLists


# Method to import Package CSV file information into a usable HashMap
def loadPackageData(fileName):
    # Create an instance of HashMap class to store package information.
    packageMap = PackageHashMap()
    # Open file to access each row and assign each row to an instance of the package class.
    with open(fileName) as packageCSV:
        packageData = csv.reader(packageCSV, delimiter=',')

        # Instantiate each row in packageData as an instance of Package, and assign each cell as a Package attr.
        for package in packageData:
            packageID = int(package[0])
            deliveryAddress = package[1]
            city = package[2]
            state = package[3]
            postCode = int(package[4])
            deliveryTime = package[5]
            weight = package[6]
            specialInstructions = package[7]

            # If specialInstructions is empty use default value, if not then assign value from CSV file.
            if specialInstructions == '':
                newPackage = Package(packageID, deliveryAddress, city, state, postCode, deliveryTime, weight)
            else:
                newPackage = Package(packageID, deliveryAddress, city, state, postCode, deliveryTime, weight,
                                     specialInstructions)

            packageMap.add(newPackage.id, newPackage)

    return packageMap

# This method takes the distances CSV file and creates / returns a list
# containing each and every address associated with the distance CSV file.
def loadAddressData(fileName):
    deliveryAddresses = []

    # With file open, read the information and extract each address.
    with open(fileName) as addressInfo:
        addressData = csv.reader(addressInfo, delimiter=',')
        # Extract each address and append to the deliveryAddresses list.
        for address in addressData:
            deliveryAddresses.append(address[0])

    return deliveryAddresses
