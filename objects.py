class Truck:
    def __init__(self,
                 truck_id,
                 location,
                 destination,
                 packages):
        self.id = truck_id
        self.location = location
        self.destination = destination
        self.mileage = 0
        self.packages = packages


class Package:
    def __init__(self,
                 package_id,
                 address,
                 deadline,
                 city,
                 zip_code,
                 weight,
                 status='AT_HUB'):
        self.id = package_id
        self.address = address
        self.deadline = deadline
        self.city = city
        self.zip_code = zip_code
        self.weight = weight
        self.status = status
