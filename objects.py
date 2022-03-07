class Truck:
    def __init__(self,
                 id,
                 location):
        self.id = id
        self.location = location
        self.mileage = 0


class Package:
    def __init__(self,
                 id,
                 address,
                 deadline,
                 city,
                 zip_code,
                 weight,
                 status):
        self.id = id
        self.address = address
        self.deadline = deadline
        self.city = city
        self.zip_code = zip_code
        self.weight = weight
        self.status = status
