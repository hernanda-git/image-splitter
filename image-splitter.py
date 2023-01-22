from PIL import Image
import argparse

# Create argument parser
parser = argparse.ArgumentParser()

# Add arguments
parser.add_argument("-i", "--image", required=True, help="Path to the image to split")
parser.add_argument("-w", "--width", type=float, required=True, help="Width percentage to split the image by. Must be between 0 and 1.")

# Parse arguments
args = parser.parse_args()

# Open image
im = Image.open(args.image)

# Get image width and height
width, height = im.size

# Set the width percentage to split the image by
width_percent = args.width

# Calculate the width and height of each new image
new_width = int(width * width_percent)
new_height = height

# Split the image and save the parts
for i in range(0, width, new_width):
    box = (i, 0, i+new_width, new_height)
    im_part = im.crop(box)
    im_part.save("image_part_{}.jpg".format(i))