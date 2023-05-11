class PackageHashMap:
    def __init__(self):
        self.size = 40
        self.map = [None] * self.size

    def getHash(self, key):
        return key % self.size

    def add(self, key, value):
        bucket = self.getHash(key)
        key_value = [key, value]

        if self.map[bucket] is None:
            self.map[bucket] = list([key_value])
            return True
        else:
            for pair in self.map[bucket]:
                if pair[0] == key:
                    pair[1] = value
                    return True
            self.map[bucket].append(key_value)
            return True

    def get(self, key):
        bucket = self.getHash(key)
        if self.map[bucket] is not None:
            for pair in self.map[bucket]:
                if pair[0] == key:
                    return pair[1]
        return None

    def remove(self, key):
        bucket = self.getHash(key)
        print(bucket)
        bucket_list = self.map[bucket]
        print(bucket_list)

        for pair in bucket_list:
            if pair[0] == key:
                print("It is")
                bucket_list.remove(pair)

    def getAddress(self, key):
        return getattr(self.get(key), 'address')

    # Updates delivery status of package in the HashMap.
    # Key is the package ID, delivered is a boolean representing if package was delivered or not.
    def updateDeliveryStatus(self, key, delivered, deliveryTime=None):
        # Use get function described above to find the package in the packageHashMap
        package = self.get(key)

        # If package is delivered, will update the delivery status and delivery time.
        if delivered:
            setattr(package, 'deliveryStatus', "Delivered")
            setattr(package, 'timeDelivered', deliveryTime)
        # If package is not delivered, but the truck has left the hub, change delivery status.
        else:
            setattr(package, 'deliveryStatus', "En Route")

        # Add updated package back to packageHashMap
        self.add(key, package)

    # This method prints all key-value pairs located in the HashMap instance.
    def printAll(self):
        print("ID | Address | Deadline | City | Postal Code | Weight | Delivery Status | Truck")
        for bucket in range(len(self.map)):
            for pair in self.map[bucket]:
                print(pair[1])

    def printBucket(self, bucket):
        for pair in self.map[bucket]:
            print(f'Key: {pair[0]}, Value: {pair[1]}')