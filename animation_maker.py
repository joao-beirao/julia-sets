import imageio
from julia_set_creator import *
from image_handling import *
import os

RANGE = 100
IMAGE_DIRECTORY = './images/'


list_of_im_paths = []


for i in range(RANGE):
    
    j=(i+1)/RANGE


    filename = "{:.7f}".format(j)
    print("Working on : "+filename)
    filename_pgm = filename+'.pgm'
    filename_png = filename+'.png'

    #generate_Julia_Image(j, 720, 720, filename_pgm, IMAGE_DIRECTORY)
    #pgm_to_png(filename_pgm,filename_png,IMAGE_DIRECTORY)
    #os.remove(IMAGE_DIRECTORY + filename_pgm)

    list_of_im_paths.append("./images/{:.7f}.png".format(j))



# Read the .png images
ims = [imageio.imread(f) for f in list_of_im_paths]
# Create the .gif file
imageio.mimwrite("animation.gif", ims)


