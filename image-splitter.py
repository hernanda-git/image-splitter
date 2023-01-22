from PIL import Image

# Open image
im = Image.open("image.jpg")

# Get image width and height
width, height = im.size

# Set the width percentage to split the image by
width_percent = 0.1

# Calculate the width and height of each new image
new_width = int(width * width_percent)
new_height = height

# Split the image and save the parts
for i in range(0, width, new_width):
    box = (i, 0, i+new_width, new_height)
    im_part = im.crop(box)
    im_part.save("image_part_{}.jpg".format(i))