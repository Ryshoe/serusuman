# Gio Pascua
# Student ID: 001188967

import helpers
import objects


def main():
    # packages = helpers.load_package_data()
    # print(packages.table)
    # for i in range(len(packages.table)):
    #     for j in range(len(packages.table[i])):
    #         key = packages.table[i][j][0]
    #         print(f'Package ID: {packages.search(key).id} '
    #               f'Address: {packages.search(key).address}')

    distances = helpers.load_distance_data()
    print(distances)
    for i in range(len(distances)):
        print(distances[i])


if __name__ == "__main__":
    main()
