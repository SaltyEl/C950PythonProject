from PackageHashMap import PackageHashMap

class Truck:
    def __init__(self):
        self.packageList = []
        self.miles = 0
        self.location = 'HUB'
        self.orderedAddresses = []

    def loadTruck(self,packageMap,numbers):
        for number in numbers:
            package = packageMap.get(number)
            self.packageList.append(package)

    def getAddressList(self):
        return self.orderedAddresses

    def getPackageCount(self):
        return len(self.packageList)

    def getPackagesOnTruck(self):
        return self.packageList



