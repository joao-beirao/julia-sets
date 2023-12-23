from tools.animation_maker import *
from tools.image_handling import *
from tools.julia_set_creator import *
from tools.menu import *


IMAGE_DIRECTORY = './images/'
VIDEO_DIRECTORY = './videos/'

def main():
    option = menu()
    os.system('cls' if os.name == 'nt' else 'clear')
    print("========================== JULIA SET GENERATOR ==========================\n\n")
    imageSize = defineSize()
    filename = defineFilename()

    if option == "00":
        #Create MP4 Video
        nFrames = defineFileFrames()
        initialPoint = createPoint("A")
        finalPoint = createPoint("B")

        generateMP4(initialPoint, finalPoint,filename,imageSize, nFrames)
    if option == "01":
        #Create GIF Video
        nFrames = defineFileFrames()
        initialPoint = createPoint("A")
        finalPoint = createPoint("B")

        generateGIF(initialPoint, finalPoint,filename,imageSize, nFrames)
        
    if option == "10":
        #Create PNG Image
        p = createPoint("")
        generatePNG(p, imageSize, filename)
    if option == "11":
        #Create PGM Image
        p= createPoint("")
        generatePGM(p, imageSize, filename)   

def generateMP4(PointA, PointB, fileName, fileSize, nFrames):
    generate_Julia_Video_MP4(PointA, PointB, nFrames,fileSize,fileName)


def generateGIF(PointA, PointB, fileName, fileSize, nFrames):
    generate_Julia_Video_GIF(PointA, PointB, nFrames,fileSize,fileName)

def generatePNG(point, size, filename):
    generate_Julia_Image_PNG(point, size, filename,IMAGE_DIRECTORY)

def generatePGM(point, size, filename):
    generate_Julia_Image_PGM(point, size, filename, IMAGE_DIRECTORY)

def createPoint(Point):
    j_re = float(input(" -> Define Julia's real constant for Point " + Point + " (between -1 and 1): "))
    j_im = float(input(" -> Define Julia's imaginary constant for Point " + Point + " (between -1 and 1): "))
    print("\n\n")
    return complex(j_re, j_im)

def defineSize():
    s = int(input(" -> Define image size (max.1000): ")) 
    print("\n\n")
    return s

def defineFilename():
    s = input(" -> File Name: ") 
    print("\n\n")
    return s

def defineFileFrames():
    s = int(input(" -> Number of Frames in Video (~100/2sec): ")) 
    print("\n\n")
    return s
##################################
if __name__ == "__main__":
    main()