from PIL import Image

def pgm_to_png(input_name, output_name, Path):

    with Image.open(Path+input_name) as im:
        im.save(Path+output_name)