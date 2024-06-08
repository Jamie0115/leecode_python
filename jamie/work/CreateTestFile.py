import random


TOTAL_ROW = 288
BUFFER_FILENAME = 'buffer'
FAM_FILENAME_LIST = ['buffer', 'FAM_2.5', 'FAM_5', 'FAM_10']
LED_COUNT = 3
path = 'C:/Users/funny/Desktop/result'


def writeCsv(folder, fileName, lines):
    targetFile = path + "/" + folder + "/" + fileName + ".csv"
    try:
        output = ""
        for line in lines:
            output += line
            output += "\n"
        writeFile = open(targetFile, "w", encoding="big5")
        writeFile.write(output)
    except FileNotFoundError:
        print("File path is not found !!")


for led in range(LED_COUNT + 1):
    if led == 0:
        continue
    for fam in FAM_FILENAME_LIST:
        resultLines = list()
        resultLines.append(",average")
        for row in range(TOTAL_ROW + 1):
            if row == 0:
                continue
            resultLines.append(str(row) + "," + str(random.randint(1000, 5000)))
        writeCsv(str(led), fam, resultLines)
