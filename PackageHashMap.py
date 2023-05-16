class PackageHashMap:
    def __init__(self):
        self.size = 40
        self.map = [None] * self.size

    def getHash(self, key):
        # Compute hash value for given key
        return key % self.size

    def add(self, key, value):
        # Get bucket based on key provided.
        bucket = self.getHash(key)
        # Create list containing key and value provided
        key_value = [key, value]

        # If bucket is empty, add key-value pair to bucket and return True.
        if self.map[bucket] is None:
            self.map[bucket] = list([key_value])
            return True
        # If bucket is not empty, continue.
        else:
            # Iterate through each pair in bucket.
            for pair in self.map[bucket]:
                # If pair key matches key provided, continue.
                if pair[0] == key:
                    # Update value in key-value pair and return True.
                    pair[1] = value
                    return True
            # If key is not found, append key-value pair to bucket.
            self.map[bucket].append(key_value)
            return True

    def get(self, key):
        # Get bucket index based on key provided.
        bucket = self.getHash(key)
        # If bucket is not empty, continue.
        if self.map[bucket] is not None:
            # Iterate through each pair in bucket.
            for pair in self.map[bucket]:
                # If pair key matches provided key, return value.
                if pair[0] == key:
                    return pair[1]
        return None

    def remove(self, key):
        # Get bucket index based on key provided.
        bucket = self.getHash(key)

        # Get the list of key-value pairs in the bucket
        bucket_list = self.map[bucket]

        # Iterate through the key-value pairs in the bucket
        for pair in bucket_list:
            # Check if current pairs key matches key provided.
            if pair[0] == key:
                # If keys match, remove pair from bucket list.
                bucket_list.remove(pair)

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