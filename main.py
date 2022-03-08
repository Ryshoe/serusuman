# Gio Pascua
# Student ID: 001188967

import helpers
import objects


def main():
    packages = helpers.HashTable.load_package_data(helpers.HashTable())
    print(packages.table)
    for i in range(len(packages.table)):
        for j in range(len(packages.table[i])):
            key = packages.table[i][j][0]
            print(f'Package ID: {packages.search(key).id} '
                  f'Address: {packages.search(key).address}')


if __name__ == "__main__":
    main()
