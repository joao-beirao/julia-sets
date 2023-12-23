import numpy as np
from tools.image_handling import *
import os

# Constants
DEFAULT_IMAGE_SIZE = 720

IMAGE_RANGE = 2.0 # Imaginary and Real Range in [-IMAGE_RANGE ; IMAGE_RANGE]
DECAY_RANGE = 5 # num of painting iterations = 255/ DECAY_RANGE
Central_Pivot = 0


# Create Julia's Graph image (julia_constant, img_size, filename)
def generate_Julia_Image_PGM(julia_point, size, filename, dir):
    re_min = -IMAGE_RANGE
    re_max = IMAGE_RANGE
    im_min = -IMAGE_RANGE
    im_max =IMAGE_RANGE

    w = size
    h = size

    fn = str(dir+filename+".pgm")
    c = julia_point

    real_range = np.arange(re_min, re_max, (re_max-re_min)/w)
    imag_range = np.arange(im_min, im_max, (im_max-im_min)/h)

    output = open(fn, "w")
    output.write('P2\n# Julia Set image\n'+str(w)+' '+str(h)+'\n255\n')

    for im in imag_range:
        for re in real_range:
            z = complex(re,im)
            n=255
            while abs(z) < 10 and n >= DECAY_RANGE:
                z = z*z + c
                n = n - DECAY_RANGE
            output.write(str(n)+' ')
        output.write('\n')

    output.close()

def generate_Julia_Image_PNG(julia_point, size, filename, directory):
    generate_Julia_Image_PGM(julia_point, size, filename, directory)
    pgm_to_png(filename+".pgm",filename+".png",directory)
    os.remove(directory+filename+".pgm")
    os.system('cls' if os.name == 'nt' else 'clear')
    print("\n\tCreated File: "+filename+".png\n")



    

