from image_handling import *
from julia_set_creator import *

IMAGE_DIRECTORY = './images/'


print("========================= Julia Image Generator =========================")
print("\n")

weight = int(input("Define image size (max.1000): "))            
height = weight #int(input("Define image height: "))
j = float(input("Define Julia's constant (between 0 and 1): "))

filename = "{:.7f}".format(j) #input("Define File Name: ")

filename_pgm = filename+'.pgm'
filename_png = filename+'.png'


generate_Julia_Image(j, weight, height, filename_pgm, IMAGE_DIRECTORY)

print("\nImages Created: \n")
print("\t-> Image generated ("+filename_pgm+")")
pgm_to_png(filename_pgm,filename_png,IMAGE_DIRECTORY)
print("\t-> Image generated ("+filename_png+")")

print("=========================================================================")