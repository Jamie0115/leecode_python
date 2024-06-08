total = 8
result = [0] * total
count = 0


def nextRow(row):
    global count
    for column in range(total):
        result[row] = column
        if isError(row):
            continue
        if row < total - 1:
            nextRow(row + 1)
        else:
            printResult()
            count = count + 1


def isError(row):
    current = result[row]
    for i in range(row):
        compare = result[i]
        offset = row - i

        if current == compare:
            return True
        if current - offset == compare:
            return True
        if current + offset == compare:
            return True


def printResult():
    print(result)
    for rowResult in result:
        line = ""
        for i in range(total):
            if rowResult == i:
                line += "Q"
            else:
                line += "*"
        print(line)
    print()


for firstRowColumn in range(total):
    result[0] = firstRowColumn
    nextRow(1)
print("總共" + str(count) + "個解")
