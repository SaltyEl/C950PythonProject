from PackageHashMap import PackageHashMap

class Truck:
    def __init__(self, name):
        self.packageList = []
        self.miles = 0
        self.location = 'HUB'
        self.orderedAddresses = []
        self.name = name

    # This method loads a truck with packages. IDs is a list of package IDs to identify
    # which packages need to be loaded. packageMap is the hashmap containing the package information.
    def loadTruck(self, packageMap, IDs):
        for ID in IDs:
            # Obtain the package
            package = packageMap.get(ID)
            # Append the package to list.
            self.packageList.append(package)

    # Returns orderedAddresses
    def getOrderedAddresses(self):
        return self.orderedAddresses

    # Returns the self.packageList
    def getPackagesOnTruck(self):
        return self.packageList

    # This function adds the truck name to each package, and then updates that information
    # in the packageHashMap
    def assignPackagesToTruck(self, packageHashMap):
        for package in self.packageList:
            package.setTruckName(self)
            packageHashMap.add(package.id, package)

