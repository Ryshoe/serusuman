import csv

from objects import Package


def load_package_data():
    # Open CSV and read into hash table
    with open('data/packages.csv') as data:
        data = csv.reader(data, delimiter=',')
        package_table = HashTable()

        for i in data:
            package_id = int(i[0])
            address = i[1]
            city = i[2]
            zip_code = i[4]
            deadline = i[5]
            weight = i[6]
            package = Package(package_id, address, deadline, city, zip_code, weight)
            package_table.insert(package_id, package)

        return package_table


def load_distance_data():
    # Open CSV and read into array list
    with open('data/distances.csv') as data:
        data = csv.reader(data, delimiter=',')
        distance_list = []

        for i in data:
            row = list(i)
            distance_list.append(row)

    return distance_list


def load_address_data():
    # Open CSV and read into array list
    with open('data/addresses.csv') as data:
        data = csv.reader(data, delimiter=',')
        address_list = []

        for i in data:
            address_list.append(i[1])

    return address_list


def get_distance(address1, address2):
    # Load CSV data
    address_list = load_address_data()
    distance_list = load_distance_data()

    # Assign indices from address list
    address1_index = address_list.index(address1)
    address2_index = address_list.index(address2)

    # Return value from distance list
    distance = distance_list[address1_index][address2_index]

    return float(distance)


def min_distance(curr_address, truck_packages, package_list):
    # Declare variable to hold the shortest distance
    shortest_distance = -1.0

    # Iterate through packages on truck and compare distances from truck's current location
    for i in range(len(truck_packages)):
        package_address = package_list.search(truck_packages[i]).address
        distance = get_distance(curr_address, package_address)

        if distance < shortest_distance or shortest_distance == -1.0:
            shortest_distance = distance

    return shortest_distance


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
