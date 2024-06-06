BUFFER_FILENAME = "buffer"
TARGET_FILENAME = "results"
FILE_FAM_FILENAME_LIST = ['FAM_2.5', 'FAM_5', 'FAM_10']
path = "/Users/erenwu/Documents/file2"


def readCsv(fileName):
    try:
        readFile = open(path + "/" + fileName + ".csv", "r", encoding="big5")
        content = readFile.read()
        rows = content.split("\n")
        rowList = list()
        for row in rows:
            if "," in row:
                columns = row.split(",")
                rowList.append({
                    "index": int(columns[0]),
                    "value": int(columns[1])
                })
        return rowList
    except FileNotFoundError as e:
        print("File path is not found !!")


def writeCsv(content, fileName):
    try:
        writeFile = open(path + "/" + fileName + ".csv", "w", encoding="big5")
        writeFile.write(content)
    except FileNotFoundError as e:
        print("File path is not found !!")


resultMap = dict()
for target in FILE_FAM_FILENAME_LIST:
    resultMap[target] = readCsv(target)

output = "Index,buffer," + ",".join(FILE_FAM_FILENAME_LIST) + "\n"
for buffer in readCsv(BUFFER_FILENAME):
    bufferIndex = buffer.get("index")
    bufferValue = buffer.get("value")
    output += str(bufferIndex) + ","
    output += str(0) + ","

    for fam in FILE_FAM_FILENAME_LIST:
        list = resultMap.get(fam)
        famValue = list[bufferIndex - 1].get("value")
        output += str(famValue - bufferValue) + ","

    output += "\n"

writeCsv(output, TARGET_FILENAME)
