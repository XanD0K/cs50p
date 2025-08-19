import sys

from PIL import Image

images = []

for arg in sys.argv[1:]:
    image = Image.open(arg)
    images.append(image)

images[0].save(
    "costumes.gif", save_all=True, append_images=[images[1]], duration=200, loop=0
)

# images[0].save() → get's the first image in the list and save it to disk. It opens, saves and closes it with just that .save() command
# "costumes.gif" → the name of the file that 
# save_all=True → tell that library to save all of the frames that will be passed to it (the 2 costume.gif files)
# append_images=[images[1]] → appends the next image to the first one
# duration=200 → happens in 200 milliseconds
# loop=0 → Loops an infinite number of times