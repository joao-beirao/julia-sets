import imageio
from tools.julia_set_creator import *
from tools.image_handling import *
from tools.progress_bar import *
import os


IMAGE_DIRECTORY = './temp/'
OUTPUT_DIRECTORY = "./videos/ "


list_of_im_paths = []

# Initial and Final are complex numbers
def calculate_Current_Frame(initial, final, nFrames, currentRow):
    real = ( ( ( complex(final).real - complex(initial).real ) / nFrames ) * currentRow) + complex(initial).real
    imag = ( ( ( complex(final).imag - complex(initial).imag ) / nFrames ) * currentRow) + complex(initial).imag
    return complex(real, imag)

# Recomended values:
#   - nFrames : 100-500
#   - resolution : 120-720
#   - filename 
#
def generate_Julia_Video_MP4(init, final, nFrames, resolution, fn):

    for i in range(nFrames):
        
        currentNumber = calculate_Current_Frame(init, final, nFrames, i)

        # Create PGM Files
        filename = str(currentNumber)
        os.system('cls' if os.name == 'nt' else 'clear')
        showProgressBar(i,nFrames)
        filename_pgm = filename+'.pgm'
        filename_png = filename+'.png'

        generate_Julia_Image_PGM(currentNumber, resolution, filename,IMAGE_DIRECTORY)

        # Convert PGMs to PGNs
        pgm_to_png(filename_pgm,filename_png,IMAGE_DIRECTORY)
        os.remove(IMAGE_DIRECTORY + filename_pgm)

        # Add PNG Paths to List
        list_of_im_paths.append(IMAGE_DIRECTORY + str(currentNumber) + ".png")
    # Read the PNG List
    ims = [imageio.imread(f) for f in list_of_im_paths]
    # Create the .gif file
    imageio.mimwrite(OUTPUT_DIRECTORY+fn+".mp4", ims)
    # Delete PNGs
    for im in list_of_im_paths:
        os.remove(im)
    os.system('cls' if os.name == 'nt' else 'clear')
    print("\n\tCreated File: "+fn+".mp4\n")

def generate_Julia_Video_GIF(init, final, nFrames, resolution, fn):

    for i in range(nFrames):
        
        currentNumber = calculate_Current_Frame(init, final, nFrames, i)

        # Create PGM Files
        filename = str(currentNumber)
        os.system('cls' if os.name == 'nt' else 'clear')
        showProgressBar(i,nFrames)
        filename_pgm = filename+'.pgm'
        filename_png = filename+'.png'

        generate_Julia_Image_PGM(currentNumber, resolution, filename, IMAGE_DIRECTORY)

        # Convert PGMs to PGNs
        pgm_to_png(filename_pgm,filename_png,IMAGE_DIRECTORY)
        os.remove(IMAGE_DIRECTORY + filename_pgm)

        # Add PNG Paths to List
        list_of_im_paths.append(IMAGE_DIRECTORY + str(currentNumber) + ".png")
    # Read the PNG List
    ims = [imageio.imread(f) for f in list_of_im_paths]
    # Create the .gif file
    imageio.mimwrite(OUTPUT_DIRECTORY+fn+".gif", ims)
    # Delete PNGs
    for im in list_of_im_paths:
        os.remove(im)
    os.system('cls' if os.name == 'nt' else 'clear')
    print("\n\tCreated File: "+fn+".gif\n")


