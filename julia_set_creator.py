import numpy as np
import os
from PIL import Image

# Constants
IMAGE_DIRECTORY_PGM = './images/pgm/'
IMAGE_DIRECTORY_PNG = './images/png/'
DEFAULT_IMAGE_SIZE = 720

IMAGE_RANGE = 2.0 # Imaginary and Real Range in [-IMAGE_RANGE ; IMAGE_RANGE]
DECAY_RANGE = 5 # num of painting iterations = 255/ DECAY_RANGE
Central_Pivot = 0.5


# Create Julia's Graph image (julia_constant, img_weight, img_height, filename)
def generate_Julia_Image(julia_constant, w, h, filename):
    re_min = -IMAGE_RANGE
    re_max = IMAGE_RANGE
    im_min = -IMAGE_RANGE
    im_max =IMAGE_RANGE

    fn = IMAGE_DIRECTORY_PGM + str(filename) + '.pgm'
    c = complex(Central_Pivot, julia_constant)

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

def pgm_to_png(filename):

    with Image.open(IMAGE_DIRECTORY_PGM+filename+'.pgm') as im:
        im.save(IMAGE_DIRECTORY_PNG+filename+'.png')

print("========================= Julia Image Generator =========================")
print("\n")

weight = DEFAULT_IMAGE_SIZE #int(input("Define image width: "))            
height = DEFAULT_IMAGE_SIZE #int(input("Define image height: "))
j = float(input("Define Julia's constant (between 0 and 1): "))

filename = input("Define File Name: ")

generate_Julia_Image(j, weight, height, filename)
print("\nImages Created: \n")
print("\t-> Image generated ("+filename+".pgm)")
pgm_to_png(filename)
print("\t-> Image generated ("+filename+".png)")

print("=========================================================================")

    

