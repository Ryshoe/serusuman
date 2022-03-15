# Gio Pascua
# Student ID: 001188967
import datetime
import helpers
import objects


def main():
    package_data = helpers.load_package_data()
    distance_data = helpers.load_distance_data()
    address_data = helpers.load_address_data()

    truck1 = objects.Truck(1, address_data[0], '', [1, 4, 6, 7, 8, 25, 26, 28, 29, 30, 31, 32, 40])
    truck2 = objects.Truck(2, address_data[0], '', [3, 5, 13, 14, 15, 16, 18, 19, 20, 21, 34, 36, 37, 38, 39])
    truck3 = objects.Truck(3, address_data[0], '', [2, 9, 10, 11, 12, 17, 22, 23, 24, 27, 33, 35])

    truck1 = helpers.deliver_packages(truck1, package_data, datetime.timedelta(hours=9, minutes=5))
    truck2 = helpers.deliver_packages(truck2, package_data, datetime.timedelta(hours=8))
    truck3 = helpers.deliver_packages(truck3, package_data, datetime.timedelta(hours=9, minutes=52, seconds=40))

    total_mileage = truck1.mileage + truck2.mileage + truck3.mileage
    print(f'Total mileage: {total_mileage}')

    print(package_data.table)
    for i in range(len(package_data.table)):
        for j in range(len(package_data.table[i])):
            key = package_data.table[i][j][0]
            print(f'Package ID: {package_data.search(key).id} '
                  f'\t|\tDeadline: {package_data.search(key).deadline} '
                  f'\nStatus: {package_data.search(key).status}')

    # print(distance_data)
    # for i in range(len(distance_data)):
    #     print(distance_data[i])

    # print(address_data)
    # for i in range(len(address_data)):
    #     print(address_data[i])

    # print(helpers.get_distance('2010 W 500 S', "4300 S 1300 E"))
    # print(helpers.min_distance('2010 W 500 S', [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]))
    # print(address_data[truck1.destination])

    # for i in range(len(package_data.table)):
    #     for j in range(len(package_data.table[i])):
    #         key = package_data.table[i][j][0]
    #         print(f'Package ID: {package_data.search(key).id} '
    #               f'Address: {package_data.search(key).address} '
    #               f'Status: {package_data.search(key).status}')


if __name__ == "__main__":
    main()
