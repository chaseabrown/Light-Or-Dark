import skimage
import numpy as np
import os
import sys

directory = os.fsencode("/Users/chaseabrown/Downloads/VisDrone2018-DET-train/images/")
numOfFiles = len(os.listdir(directory))
counter = 0
for file in os.listdir(directory):
    counter += 1
    filename = os.fsdecode(file)
    if (filename.endswith(".jpg") or filename.endswith(".JPG")):
        try:
            image = skimage.io.imread("./images/" + filename)
            imageg = skimage.color.rgb2grey(image)
            imagef = skimage.img_as_float(imageg)
            if(np.mean(imagef)<.2685):
                skimage.io.imsave("./DarkImagesTrain/" + filename, image)
            else:
                skimage.io.imsave("./LightImagesTrain/" + filename, image)
            print(str(counter) + " out of " + str(numOfFiles))
        except:
            print("Error with: " + filename)
            print(os.path.abspath(filename))
            print(sys.exc_info())


