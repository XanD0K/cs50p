from pathlib import Path
from PIL import Image, ImageOps, UnidentifiedImageError

import sys


EXTENSIONS = ['.jpeg', '.jpg', '.png']

def main():
    # Must have exactly 3 command line arguments
    if len(sys.argv) != 3:
        sys.exit("Usage: 'python shirt.py <image1_name> <image2_name>'. That image can be of JPEG, JPG or PNG format")

    input_path = Path(sys.argv[1])
    output_path = Path(sys.argv[2])

    # Input and output must be of the JPG, JPEG or PNG extension
    # I can also get the extension by using 'os.path.splitext'
    if not (input_path.suffix.lower() in EXTENSIONS or output_path.suffix.lower() in EXTENSIONS):
        sys.exit("Image must be of JPEG, JPG or PNG format")

    # Input's and output's extensions must be the same
    if not (input_path.suffix.lower() == output_path.suffix.lower()):
        sys.exit("Input and Output msut have the same extension")

    # Check if input file exists
    if not input_path.is_file():
        sys.exit(f"File {sys.argv[1]} does not exist!")

    # Check if shirt image exists
    shirt_path = Path("shirt.png")
    if not shirt_path.is_file():
        sys.exit("shit.png does not exist in current directory")

    try:
        # Open, modify and save input image
        with Image.open(input_path) as input_image:
            with Image.open(shirt_path) as shirt_image:
                input_image = ImageOps.fit(input_image, size=shirt_image.size)
                input_image.paste(shirt_image, shirt_image)
                input_image.save(f"{sys.argv[2]}")
    except FileNotFoundError:
        sys.exit(f"Cannot write to {output_path}! Output directory does not exist")
    except PermissionError:
        sys.exit(f"Permission denied acessing {input_path}, {shirt_path}, or {output_path}")
    except (OSError, UnidentifiedImageError, ValueError) as e:
        sys.exit(f"Error processing that image: {e}")

if __name__ == "__main__":
    main()