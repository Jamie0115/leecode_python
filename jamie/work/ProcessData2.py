import csv


def getWavelengthDict(rowData):
    returnDict = dict()
    for pixel in range(1, 289):
        A0 = float(rowData['A0'])
        B1 = float(rowData['B1'])
        B2 = float(rowData['B2'])
        B3 = float(rowData['B3'])
        B4 = float(rowData['B4'])
        B5 = float(rowData['B5'])
        wavelength = (A0
                      + (B1 * pixel)
                      + (B2 * pixel ** 2)
                      + (B3 * pixel ** 3)
                      + (B4 * pixel ** 4)
                      + (B5 * pixel ** 5))
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
