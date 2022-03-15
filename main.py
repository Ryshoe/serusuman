# Gio Pascua
# Student ID: 001188967
from datetime import datetime
import helpers
from objects import Truck


def main():
    package_data = helpers.load_package_data()
    distance_data = helpers.load_distance_data()
    address_data = helpers.load_address_data()

    truck1 = Truck(1, '4001 South 700 East', '', [1, 4, 6, 7, 8, 25, 26, 28, 29, 30, 31, 32, 40])
    truck2 = Truck(2, '4001 South 700 East', '', [3, 5, 13, 14, 15, 16, 18, 19, 20, 21, 34, 36, 37, 38, 39])
    truck3 = Truck(3, '4001 South 700 East', '', [2, 9, 10, 11, 12, 17, 22, 23, 24, 27, 33, 35])

    # package = package_data.search(39)
    # package.status = f'DELIVERED at {datetime.now()}'

    # print(package_data.table)
    # for i in range(len(package_data.table)):
    #     for j in range(len(package_data.table[i])):
    #         key = package_data.table[i][j][0]
    #         print(f'Package ID: {package_data.search(key).id} '
    #               f'Address: {package_data.search(key).address} '
    #               f'Status: {package_data.search(key).status}')

    # print(distance_data)
    # for i in range(len(distance_data)):
    #     print(distance_data[i])

    # print(address_data)
    # for i in range(len(address_data)):
    #     print(address_data[i])

    # print(helpers.get_distance('2010 W 500 S', "4300 S 1300 E"))
    # print(helpers.min_distance('2010 W 500 S', [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]))
    # print(address_data[truck1.destination])

    print(truck1.mileage)
    truck1 = helpers.deliver_packages(truck1, package_data)
    print(truck1.mileage)

    print(truck2.mileage)
    truck1 = helpers.deliver_packages(truck2, package_data)
    print(truck2.mileage)

    print(truck3.mileage)
    truck1 = helpers.deliver_packages(truck3, package_data)
    print(truck3.mileage)

    # for i in range(len(package_data.table)):
    #     for j in range(len(package_data.table[i])):
    #         key = package_data.table[i][j][0]
    #         print(f'Package ID: {package_data.search(key).id} '
    #               f'Address: {package_data.search(key).address} '
    #               f'Status: {package_data.search(key).status}')


if __name__ == "__main__":
    main()
