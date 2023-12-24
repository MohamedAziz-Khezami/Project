import sys
import os
from PIL import Image, ImageOps


end = [".jpg", ".jpeg", ".png"]


if len(sys.argv) > 3:
    sys.exit("Too many command-line arguments")
elif len(sys.argv) < 3:
    sys.exit("Too few command-line arguments")
elif os.path.splitext(sys.argv[1])[1] != os.path.splitext(sys.argv[2])[1]:
    sys.exit("Input and output have different extensions")
elif (os.path.splitext(sys.argv[1])[1] not in end) or (
    os.path.splitext(sys.argv[2])[1] not in end
):
    sys.exit("Invalid output")

else:
    try:
        image = Image.open(sys.argv[1])

    except FileNotFoundError:
        sys.exit("Input does not exist")


shirt = Image.open("shirt.png")

resized_image = ImageOps.fit(image, shirt.size)

resized_image.paste(shirt, mask=shirt)

resized_image.save(sys.argv[2])
