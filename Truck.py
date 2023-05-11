from PackageHashMap import PackageHashMap

class Truck:
    def __init__(self, name):
        self.packageList = []
        self.miles = 0
        self.location = 'HUB'
        self.orderedAddresses = []
        self.name = name

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

    def assignPackagesToTruck(self, packageData):
        for package in self.packageList:
            package.setTruckName(self)
            packageData.add(package.id, package)

