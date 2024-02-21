import sys
from os import path
from PIL import Image


def get_format(name):
    if name.endswith('.jpg') or name.endswith('.jpeg'):
        return 'jpg'
    elif name.endswith('.png'):
        return 'png'
    else:
        sys.exit("Invalid input")


# Handle command-line arguments
if len(sys.argv) < 3:
    sys.exit("Too few command-line arguments")
elif len(sys.argv) > 3:
    sys.exit("Too many command-line arguments")

read_pic_name = sys.argv[1].lower()
write_pic_name = sys.argv[2].lower()

if not path.exists(read_pic):
    sys.exit("File does not exist")

read_pic_format = get_format(read_pic)
write_pic_format = get_format(write_pic)

if not read_pic_format == write_pic_format: #potential to shorten!
     sys.exit("Input and output have different extensions")


# Change below
images = []


for arg in sys.argv[1:]:
	image = Image.open(arg)
	images.append(image)

images[0].save(
	"costumes.gif", save_all=True, append_images=[images[1]], duration=200, loop=0
)