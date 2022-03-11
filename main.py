# Gio Pascua
# Student ID: 001188967

import helpers
import objects


def main():
    package_list = helpers.load_package_data()
    distance_list = helpers.load_distance_data()
    address_list = helpers.load_address_data()

    # print(package_list.table)
    # for i in range(len(package_list.table)):
    #     for j in range(len(package_list.table[i])):
    #         key = package_list.table[i][j][0]
    #         print(f'Package ID: {package_list.search(key).id} '
    #               f'Address: {package_list.search(key).address} '
    #               f'Status: {package_list.search(key).status}')

    # print(distance_list)
    # for i in range(len(distance_list)):
    #     print(distance_list[i])

    # print(address_list)
    # for i in range(len(address_list)):
    #     print(address_list[i])

    # print(helpers.get_distance('2010 W 500 S', "4300 S 1300 E"))
    # print(helpers.min_distance('2010 W 500 S', [1, 2, 3, 4, 5, 6, 7], package_list))

if __name__ == "__main__":
    main()
