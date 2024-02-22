import sys
from os import path
from PIL import Image, ImageOps


def get_format(name):
    if name.endswith('.jpg') or name.endswith('.jpeg'):
        return 'jpg'
    elif name.endswith('.png'):
        return 'png'
    else:
        sys.exit("Invalid input")

def main():
    # Handle command-line arguments
    if len(sys.argv) < 3:
        sys.exit("Too few command-line arguments")
    elif len(sys.argv) > 3:
        sys.exit("Too many command-line arguments")

    read_pic_name = sys.argv[1].lower()
    write_pic_name = sys.argv[2].lower()

    if not path.exists(read_pic_name):
        sys.exit("File does not exist")

    if get_format(read_pic_name) != get_format(write_pic_name):
        sys.exit("Input and output have different extensions")


    # Open shirt.png and before image
    shirt_pic = Image.open('shirt.png')
    read_pic = Image.open(read_pic_name)

    # Resize read_pic to match shirt_pic's size
    write_pic = ImageOps.fit(read_pic, shirt_pic.size)

    # Overlay shirt.png onto write_pic
    write_pic.paste(shirt_pic, (0, 0))

    # Save pic
    write_pic.save(write_pic_name)


if __name__ == "__main__":
    main()