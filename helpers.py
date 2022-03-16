import csv
import datetime

from objects import Package


def load_package_data():
    # Open CSV and read into hash table
    with open('data/packages.csv') as data:
        data = csv.reader(data, delimiter=',')
        package_data = HashTable()

        for i in data:
            package_id = int(i[0])
            address = i[1]
            city = i[2]
            zip_code = i[4]
            deadline = i[5]
            weight = i[6]
            package = Package(package_id, address, deadline, city, zip_code, weight)
            package_data.insert(package_id, package)

        return package_data


def load_distance_data():
    # Open CSV and read into array list
    with open('data/distances.csv') as data:
        data = csv.reader(data, delimiter=',')
        distance_data = []

        for i in data:
            row = list(i)
            distance_data.append(row)

    return distance_data


def load_address_data():
    # Open CSV and read into array list
    with open('data/addresses.csv') as data:
        data = csv.reader(data, delimiter=',')
        address_data = []

        for i in data:
            address_data.append(i[1])

    return address_data


def get_distance(address1, address2):
    # Load CSV data
    address_data = load_address_data()
    distance_data = load_distance_data()

    # Assign indices from address list
    address1_index = address_data.index(address1)
    address2_index = address_data.index(address2)

    # Return value from distance list
    distance = distance_data[address1_index][address2_index]

    return float(distance)


def min_distance(curr_address, truck_packages):
    # Declare variables to hold the shortest distance and closest address
    shortest_distance = -1.0
    closest_address = ""

    # Iterate through packages on truck and compare distances from truck's current location
    package_data = load_package_data()
    for i in range(len(truck_packages)):
        package_address = package_data.search(truck_packages[i]).address
        distance = get_distance(curr_address, package_address)

        if distance < shortest_distance or shortest_distance == -1.0:
            shortest_distance = distance
            closest_address = package_address

    return closest_address


def deliver_packages(truck, package_data, depart_time):
    # Update all packages to 'EN_ROUTE'
    for i in range(len(truck.packages)):
        key = truck.packages[i]
        package = package_data.search(key)
        package.departed_at = depart_time
        package.status = 'EN_ROUTE'

    while truck.packages:
        # Get the closest address from packages
        truck.destination = min_distance(truck.location, truck.packages)

        # Increment truck mileage and current time based on distance
        truck.mileage += get_distance(truck.location, truck.destination)
        time_elapsed = get_distance(truck.location, truck.destination) / truck.speed
        depart_time += datetime.timedelta(hours=time_elapsed)

        # Drive truck to destination
        truck.location = truck.destination

        # Deliver packages that belong to current address
        for i in range(len(truck.packages) - 1, -1, -1):
            key = truck.packages[i]
            package = package_data.search(key)

            if truck.location == package.address:
                package.delivered_at = depart_time
                package.status = f'DELIVERED'
                del truck.packages[i]

    else:
        # Return truck to hub once package list is exhausted
        truck.destination = '4001 South 700 East'
        truck.mileage += get_distance(truck.location, truck.destination)
        truck.location = truck.destination

    # Print truck's return time
    print(f'Truck #{truck.id} returned to hub at: {depart_time}')
    return truck


def package_status_by_id(package_data, id_input):
    # Loop through hash table
    for i in range(len(package_data.table)):
        for j in range(len(package_data.table[i])):
            key = package_data.table[i][j][0]

            # Output package details if input matches
            if package_data.search(key).id == id_input:
                print(f'Package ID: {package_data.search(key).id}'
                      f'\nDelivery address: {package_data.search(key).address}'
                      f'\nDelivery deadline: {package_data.search(key).deadline}'
                      f'\nDelivery city: {package_data.search(key).city}'
                      f'\nDelivery zip code: {package_data.search(key).zip_code}'
                      f'\nPackage weight: {package_data.search(key).weight} kg')
                if package_data.search(key).status == 'DELIVERED':
                    print(f'Delivery status: {package_data.search(key).status}'
                          f' at {package_data.search(key).delivered_at}')
                else:
                    print(f'Delivery status: {package_data.search(key).status}')


def package_status_all(package_data, time_input):
    # Parse input time as HH:MM
    date_time_obj = datetime.datetime.strptime(time_input, '%H:%M')
    time_delta_obj = datetime.timedelta(hours=date_time_obj.hour, minutes=date_time_obj.minute)

    # Loop through hash table
    for i in range(len(package_data.table)):
        for j in range(len(package_data.table[i])):
            key = package_data.table[i][j][0]

            # Output text based on package's current status
            if package_data.search(key).departed_at > time_delta_obj:
                print(f'Package {package_data.search(key).id}: AT_HUB')
            elif package_data.search(key).departed_at <= time_delta_obj < package_data.search(key).delivered_at:
                print(f'Package {package_data.search(key).id}: EN_ROUTE')
            else:
                print(f'Package {package_data.search(key).id}: DELIVERED at {package_data.search(key).delivered_at}')


class HashTable:
    def __init__(self, initial_capacity=10):
        self.table = []
        for i in range(initial_capacity):
            self.table.append([])

    def insert(self, key, value):
        bucket = hash(key) % len(self.table)
        bucket_list = self.table[bucket]

        for kv in bucket_list:
            if kv[0] == key:
                kv[1] = value
                return True

        key_value = [key, value]
        bucket_list.append(key_value)

    def search(self, key):
        bucket = hash(key) % len(self.table)
        bucket_list = self.table[bucket]

        for key_value in bucket_list:
            if key_value[0] == key:
                return key_value[1]

        return None

    def remove(self, key):
        bucket = hash(key) % len(self.table)
        bucket_list = self.table[bucket]

        for kv in bucket_list:
            if kv[0] == key:
                bucket_list.remove([kv[0], kv[1]])

    def bucket(self, key):
        bucket = hash(key) % len(self.table)
        return bucket
