TOTAL_ROW = 288
BUFFER_FILENAME = 'buffer'
TARGET_FILENAME = 'results'
FAM_FILENAME_LIST = ['buffer', 'FAM_2.5', 'FAM_5', 'FAM_10']
LED_COUNT = 3
path = 'C:/Users/funny/Desktop/result'


def readCsv(folder, fileName):
    folder = "" if folder == "" else ("/" + folder)
    try:
        readFile = open(path + folder + "/" + fileName + ".csv", "r", encoding="big5")
        content = readFile.read()
        rows = content.split("\n")
        rowMap = dict()
        for row in rows:
            if "," in row:
                columns = row.split(",")
                key = columns[0]
                value = columns[1]
                if key.isdigit():
                    rowMap[int(key)] = int(value)
        return rowMap
    except FileNotFoundError:
        print("File path is not found !!")


def writeCsv(lines):
    try:
        output = ""
        for line in lines:
            output += line
            output += "\n"
        writeFile = open(path + "/" + TARGET_FILENAME + ".csv", "w", encoding="big5")
        writeFile.write(output)
    except FileNotFoundError:
        print("File path is not found !!")


def appendData(resultLine, dataMap, bufferMap):
    for row in dataMap:
        resultLine[row] = resultLine[row] + str(dataMap.get(row) - bufferMap.get(row)) + ","


resultLine = list()
resultLine.append("Row,")
for i in range(TOTAL_ROW + 1):
    resultLine.append(str(i) + ",")

for led in range(LED_COUNT + 1):
    if led == 0:
        continue
    # 先讀取buffer檔
    bufferMap = readCsv(str(led), BUFFER_FILENAME)

    # 再讀取該LED的每個FAM檔案
    for fam in FAM_FILENAME_LIST:
        title = fam + "_" + str(led)
        resultLine[0] = resultLine[0] + title + ","

        famMap = readCsv(str(led), fam)
        appendData(resultLine, famMap, bufferMap)


writeCsv(resultLine)
