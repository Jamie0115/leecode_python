import csv


def getWavelengthDict(rowData):
    returnDict = dict()
    for pixel in range(1, 289):
        a0 = float(rowData['A0'])
        b1 = float(rowData['B1'])
        b2 = float(rowData['B2'])
        b3 = float(rowData['B3'])
        b4 = float(rowData['B4'])
        b5 = float(rowData['B5'])
        wavelength = a0 + (b1 * pixel) + (b2 * pixel ** 2) + (b3 * pixel ** 3) + (b4 * pixel ** 4) + (b5 * pixel ** 5)
        returnDict[pixel] = wavelength
    return returnDict


FILE_PATH = "/Users/erenwu/GitHub/leecode_python/jamie/work/Test"
FILE_NAME = "Demo.csv"
MODEL_COLUMN = "光譜儀型號"

models = dict()
with open(FILE_PATH + "/" + FILE_NAME, "r") as csvFile:
    reader = csv.DictReader(csvFile)
    for row in reader:
        modelName = row[MODEL_COLUMN]
        models[modelName] = getWavelengthDict(row)

outputLines = list()
outputLines.append("pixel,")
for pixel in range(1, 289):
    outputLines.append(str(pixel) + ",")

for modelName in models:
    model = models.get(modelName)
    outputLines[0] = outputLines[0] + modelName + ","
    for pixel in range(1, 289):
        outputLines[pixel] = outputLines[pixel] + str(model.get(pixel)) + ","

with open(FILE_PATH + "/result.csv", "w") as resultFile:
    output = ""
    for line in outputLines:
        output += (line[:-1] if line[-1] == "," else line) + "\n"
    resultFile.write(output)
