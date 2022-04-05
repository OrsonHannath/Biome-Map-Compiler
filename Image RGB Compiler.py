from imageio import v3 as iio
from pathlib import Path
import io
import os
from PIL import Image
import numpy as np

rIndex = 0
gIndex = 1
bIndex = 2

thisDir = os.getcwd()

# This produces an array of 2D arrays which stores the RGB values of each Moisture image
imagesMoist = list()
for file in Path(thisDir + r"\DataFiles\Moisture").iterdir():
    im = iio.imread(file)
    imagesMoist.append(im)

# This produces an array of 2D arrays which stores the RGB values of each Heat image
imagesHeat = list()
for file in Path(thisDir + r"\DataFiles\Heat").iterdir():
    im = iio.imread(file)
    imagesHeat.append(im)

# This adds the RGB values of each pixel to a new array for Moisture Image
moistureImage = np.copy(imagesMoist[0])
rgbIndexMoist = 0
rgbFoundMoist = False

# Set the moistureImage to a White Image
for x in range(50):
    for y in range(50):
        for z in range(3):
            moistureImage[x][y][z] = 0  # Set RGB values to 0

        moistureImage[x][y][3] = 255  # Set Opacity to 255

for image in imagesMoist:
    for x in range(50):
        for y in range(50):
            if image[x][y][rIndex] > 0:
                rgbIndexMoist = rIndex
                rgbFoundMoist = True
            elif image[x][y][gIndex] > 0:
                rgbIndexMoist = gIndex
                rgbFoundMoist = True
            elif image[x][y][bIndex] > 0:
                rgbIndexMoist = bIndex
                rgbFoundMoist = True
            else:
                rgbFoundMoist = False

            if rgbFoundMoist:
                moistureImage[x][y][rgbIndexMoist] = image[x][y][rgbIndexMoist]
                # print(moistureImage[x][y])

# This adds the RGB values of each pixel to a new array for Heat Image
heatImage = np.copy(imagesHeat[0])
rgbIndexHeat = 0
rgbFoundHeat = False

# Set the moistureImage to a White Image
for x in range(50):
    for y in range(50):
        for z in range(3):
            heatImage[x][y][z] = 0  # Set RGB values to 0

        heatImage[x][y][3] = 255  # Set Opacity to 255

for image in imagesHeat:
    for x in range(50):
        for y in range(50):
            if image[x][y][rIndex] > 0:
                rgbIndexHeat = rIndex
                rgbFoundHeat = True
            elif image[x][y][gIndex] > 0:
                rgbIndexHeat = gIndex
                rgbFoundHeat = True
            elif image[x][y][bIndex] > 0:
                rgbIndexHeat = bIndex
                rgbFoundHeat = True
            else:
                rgbFoundHeat = False

            if rgbFoundHeat:
                heatImage[x][y][rgbIndexHeat] = image[x][y][rgbIndexHeat]
                # print(heatImage[x][y])

# This Averages the colours from both image maps to create a final image map
finalImage = imagesMoist[0]

# Set the finalImage to a White Image
for x in range(50):
    for y in range(50):
        for z in range(3):
            finalImage[x][y][z] = 0  # Set RGB values to 0

        finalImage[x][y][3] = 255  # Set Opacity to 255

# Loop that averages the colour from each map
for x in range(50):
    for y in range(50):
        for z in range(3):
            finalImage[x][y][z] = int((int(heatImage[x][y][z]) + int(moistureImage[x][y][z])) / 2)

# Converts from final image map to Image File
img = Image.fromarray(finalImage, 'RGBA')
img.save('BiomeTextureMap.png')
img.show()

# Converts from final image map to Image File
img2 = Image.fromarray(heatImage, 'RGBA')
img2.save('HeatTextureMap1.png')
img2.show()

# Converts from final image map to Image File
img3 = Image.fromarray(moistureImage, 'RGBA')
img3.save('MoistureTextureMap1.png')
img3.show()
