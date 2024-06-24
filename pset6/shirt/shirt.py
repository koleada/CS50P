from PIL import Image, ImageOps
import PIL
import sys

if len(sys.argv) < 3:
    exit("Too few command-line arguments")
elif len(sys.argv) > 3:
    exit("Too many command-line arguments")
else:
    input = sys.argv[1]
    output = sys.argv[2]

    # Note that you can determine a file’s extension with os.path.splitext - found out after this was written lol
    # can also use str.endswith(".jpg")

    if (
        input[-4:].lower() != ".jpg"
        and input[-4:].lower() != ".png"
        and input[-5:] != ".jpeg"
    ):
        exit("Invalid Input")
    else:
        in_ext = input[-4:].lower()
        out_ext = output[-4:].lower()

        if in_ext == ".jpg" and out_ext != ".jpg":
            exit("Input and output have different extensions")
        elif in_ext == ".png" and out_ext != ".png":
            exit("Input and output have different extensions")
        elif input[-5:].lower() == ".jpeg" and output[-4:].lower() != ".jpeg":
            exit("Input and output have different extensions")
        else:

            shirt = Image.open("shirt.png")

            try:
                inputImg = Image.open(input)
            except FileNotFoundError:
                exit("Input does not exist")

            size = shirt.size
            inputImg = ImageOps.fit(inputImg, size)
            inputImg.paste(shirt, shirt)
            inputImg.save(output)
