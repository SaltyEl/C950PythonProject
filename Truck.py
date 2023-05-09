from PackageHashMap import PackageHashMap

class Truck:
    def __init__(self):
        self.packageList = []
        self.speed = 18
        self.miles = 0
        self.location = 'HUB'

    def loadTruck(self,packageMap,numbers):
        for number in numbers:
            package = packageMap.get(number)
            self.packageList.append(package)

    def getPackageCount(self):
        return len(self.packageList)

    def getPackagesOnTruck(self):
        return self.packageList



