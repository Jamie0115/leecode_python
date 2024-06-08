import sys


def readCsv(path, folder, fileName):
    folderPath = path + "/" + folder
    try:
        readFile = open(folderPath + "/" + fileName + ".csv", "r", encoding="big5")  # "r"代表讀取的意思
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


def writeCsv(path, folder, fileName, lines):
    folderPath = path + ("" if folder == "" else ("/" + folder))
    try:
        output = ""
        for line in lines:
            output += line
            output += "\n"
        writeFile = open(folderPath + "/" + fileName + ".csv", "w", encoding="big5")  # "w"代表寫的意思
        writeFile.write(output)
    except FileNotFoundError:
        print("File path is not found !!")


TOTAL_ROW = 288
BUFFER_FILENAME = 'buffer'
TARGET_FILENAME = 'results'

sysList = sys.argv[1:]
FILE_PATH = sysList[0]
LED_COUNT = int(sysList[1])
FAM_FILENAME_LIST = list()

FAM_FILENAME_LIST.append(BUFFER_FILENAME)
for fanFileName in sysList[2].split(","):
    FAM_FILENAME_LIST.append(fanFileName)


resultLine = list()
resultLine.append("Row,")
for i in range(TOTAL_ROW + 1):
    resultLine.append(str(i) + ",")

for led in range(LED_COUNT + 1):
    if led == 0:
        continue
    # 先讀取buffer檔
    bufferMap = readCsv(FILE_PATH, str(led), BUFFER_FILENAME)

    # 再讀取該LED的每個FAM檔案
    for fam in FAM_FILENAME_LIST:
        title = fam + "_" + str(led)
        resultLine[0] = resultLine[0] + title + ","

        famMap = readCsv(FILE_PATH, str(led), fam)
        for famRow in famMap:
            resultLine[famRow] = resultLine[famRow] + str(famMap.get(famRow) - bufferMap.get(famRow)) + ","


writeCsv(FILE_PATH, "", TARGET_FILENAME, resultLine)
print("Process Data Successfully")
