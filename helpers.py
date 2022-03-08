import csv

from objects import Package


def load_package_data():
    with open('data/packages.csv') as data:
        data = csv.reader(data, delimiter=',')
        hash_table = HashTable()

        for i in data:
            package_id = int(i[0])
            address = i[1]
            city = i[2]
            zip_code = i[4]
            deadline = i[5]
            weight = i[6]
            package = Package(package_id, address, deadline, city, zip_code, weight)
            hash_table.insert(package_id, package)

        return hash_table


def load_distance_data():
    with open('data/distances.csv') as data:
        data = csv.reader(data, delimiter=',')
        distance_list = []

        for i in data:
            row = list(i)
            distance_list.append(row)

    return distance_list


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
