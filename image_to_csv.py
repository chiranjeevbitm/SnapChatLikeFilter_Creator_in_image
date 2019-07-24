from PIL import Image
import numpy as np
im = Image.open('outputfile.png')

pixels = list(im.getdata())
width, height = im.size
pixels = [pixels[i * width:(i + 1) * width] for i in xrange(height)]
#pixels = numpy.asarray(im)

np.savetxt("pixel_data.csv", pixels, delimiter=",")
