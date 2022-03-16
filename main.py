# Gio Pascua
# Student ID: 001188967
import datetime
import helpers
import objects
import sys
import os
import argparse


def main():
    # Create data objects to hold package info, distances, and addresses
    package_data = helpers.load_package_data()
    distance_data = helpers.load_distance_data()
    address_data = helpers.load_address_data()

    # Create trucks and load with packages by id
    truck1 = objects.Truck(1, address_data[0], '', [1, 4, 6, 7, 8, 25, 26, 28, 29, 30, 31, 32, 40])
    truck2 = objects.Truck(2, address_data[0], '', [3, 5, 13, 14, 15, 16, 18, 19, 20, 21, 34, 36, 37, 38, 39])
    truck3 = objects.Truck(3, address_data[0], '', [2, 9, 10, 11, 12, 17, 22, 23, 24, 27, 33, 35])

    # Send each truck to deliver its packages at a specified time
    truck1 = helpers.deliver_packages(truck1, package_data, datetime.timedelta(hours=9, minutes=5))
    truck2 = helpers.deliver_packages(truck2, package_data, datetime.timedelta(hours=8))
    truck3 = helpers.deliver_packages(truck3, package_data, datetime.timedelta(hours=9, minutes=52, seconds=40))

    # total_mileage = truck1.mileage + truck2.mileage + truck3.mileage
    # print(f'Total mileage: {total_mileage}')
    # helpers.package_status_by_id(package_data, 15)
    # helpers.package_status_all(package_data, '8:00')

    # Main menu for CLI
    print('WGU Postal Service')
    print('\n1) View package by id'
          '\n2) View all packages'
          '\n3) Exit')
    val = int(input("\nPlease select a menu option: "))

    # Retrieve user input to select menu option
    while val != 1 and val != 2 and val != 3:
        val = int(input("Invalid syntax. Please select a menu option: "))

    if val == 1:
        # Search by package id
        os.system('cls')
        input_id = int(input("Enter package id: "))
        print('')
        helpers.package_status_by_id(package_data, input_id)
        input("\nPress ENTER to exit.")
        sys.exit(1)
    elif val == 2:
        # Search all packages by given time
        os.system('cls')
        input_id = input("Enter time as (HH:MM): ")
        print('')
        helpers.package_status_all(package_data, input_id)
        input("\nPress ENTER to exit.")
        sys.exit(2)
    elif val == 3:
        sys.exit(3)


if __name__ == "__main__":
    main()
