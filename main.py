# Gio Pascua
# Student ID: 001188967
import datetime
import helpers
import objects


def main():
    # Create data objects to hold package info, distances, and addresses
    package_data = helpers.load_package_data()
    distance_data = helpers.load_distance_data()
    address_data = helpers.load_address_data()

    # Create trucks and load with packages by id
    truck1 = objects.Truck(1, address_data[0], '', [1, 4, 6, 7, 8, 25, 26, 28, 29, 30, 31, 32, 40])
    truck2 = objects.Truck(2, address_data[0], '', [3, 5, 13, 14, 15, 16, 18, 19, 20, 21, 34, 36, 37, 38, 39])
    truck3 = objects.Truck(3, address_data[0], '', [2, 9, 10, 11, 12, 17, 22, 23, 24, 27, 33, 35])

    # Send each truck to deliver its packages
    truck1 = helpers.deliver_packages(truck1, package_data, datetime.timedelta(hours=9, minutes=5))
    truck2 = helpers.deliver_packages(truck2, package_data, datetime.timedelta(hours=8))
    truck3 = helpers.deliver_packages(truck3, package_data, datetime.timedelta(hours=9, minutes=52, seconds=40))

    # total_mileage = truck1.mileage + truck2.mileage + truck3.mileage
    # print(f'Total mileage: {total_mileage}')

    # print(package_data.table)
    # for i in range(len(package_data.table)):
    #     for j in range(len(package_data.table[i])):
    #         key = package_data.table[i][j][0]
    #         print(f'Package ID: {package_data.search(key).id} '
    #               f'\t|\tDeadline: {package_data.search(key).deadline} '
    #               f'\nDEPARTED at {package_data.search(key).departed_at}'
    #               f'\n{package_data.search(key).status} '
    #               f'at {package_data.search(key).delivered_at}')

    # helpers.package_status_by_id(package_data, 15)
    # helpers.package_status_all(package_data, '8:00')


if __name__ == "__main__":
    main()
