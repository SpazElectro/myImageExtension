def getProperties(fileData):
    p = {"width": 0, "height": 0}

    index = 0

    for properties in fileData:
        index += 1

        if properties == "]":
            p["width"] = fileData.split("!", 1)[1]
            p["height"] = p["width"].split("!", 1)[1]
            p["width"] = p["width"][:-4]

    return p


def findPixels(fileData):
    pixelsStart = 0
    pixelsEnd = 0

    pixelsArray = []

    for index, pixels in enumerate(fileData):
        if pixels == "[":
            pixelsStart = index
        elif pixels == "]":
            pixelsEnd = index

    for pixelsIndex, pixels in enumerate(fileData[pixelsStart:pixelsEnd:1]):
        if pixels == "@":
            data = [
                fileData[pixelsIndex + 1 : pixelsIndex + 4],
                fileData[pixelsIndex + 4 : pixelsIndex + 3 + 4],
                fileData[pixelsIndex + 7 : pixelsIndex + 4 + 6],
            ]

            pixelsArray.append(data)

    for toParse in pixelsArray:
        toParse[0] = int(toParse[0])
        toParse[1] = int(toParse[1])
        toParse[2] = int(toParse[2])

    return pixelsArray


def openFile(fileName):
    fileData = None
    pixels = None
    properties = None

    with open(fileName, "r") as file:
        fileData = file.read()
        pixels = findPixels(fileData)
        properties = getProperties(fileData)

        file.close()

    return {
        "pixels": pixels,
        "width": properties["width"],
        "height": properties["height"],
    }