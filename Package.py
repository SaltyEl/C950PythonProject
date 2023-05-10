class Package:
    def __init__(self, id, address, city, state, zip, time, weight, instructions=None, deliveryStatus="At The Hub"):
        self.timeDelivered = None
        self.id = id
        self.address = address
        self.city = city
        self.state = state
        self.zip = zip
        self.time = time
        self.weight = weight
        self.instructions = instructions
        self.deliveryStatus = deliveryStatus

    def __str__(self):
        if self.timeDelivered != None:
            return f'{self.id} | {self.address} | {self.time} | {self.city} | {self.zip} | {self.weight} | {self.deliveryStatus} - {self.timeDelivered}'
        else:
            return f'{self.id} | {self.address} | {self.time} | {self.city} | {self.zip} | {self.weight} | {self.deliveryStatus}'
