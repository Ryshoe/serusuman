import helpers

testData = [
    [1, 'Package 1'],
    [2, 'Package 2'],
    [3, 'Package 3'],
    [4, 'Package 4'],
    [5, 'Package 5'],
    [6, 'Package 6'],
    [7, 'Package 7'],
    [8, 'Package 8'],
    [9, 'Package 9'],
    [10, 'Package 10'],
    [11, 'Package 11']
]


def main():
    myHash = helpers.ChainingHashTable()
    print(myHash.table)

    for kv in range(len(testData)):
        myHash.insert(testData[kv][0], testData[kv][1])
    print(myHash.table)

    print(myHash.search(11))

    for kv in range(len(testData)):
        myHash.remove(testData[kv][0])
    print(myHash.table)


if __name__ == "__main__":
    main()
