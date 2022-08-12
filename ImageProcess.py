from PIL import Image


def make_square(im, min_size=1080, fill_color=(0, 0, 0, 0)):
    """
    Makes the image (im) given from the user and formats it for instagram upload
    if aspect ratio is weird it makes a square of color (fill_color) and fits the image
    in it with no distortion.
    """

    x, y = im.size
    size = max(min_size, x, y)
    new_im = Image.new('RGB', (size, size), fill_color)
    if x > y:
        mod = size/x
        x = int(x * mod)
        y = int(y * mod)
    elif x < y:
        mod = size/y
        x = int(x * mod)
        y = int(y * mod)

    new_im.paste(im.resize((x,y)), (int((size - x) / 2), int((size - y) / 2)))
    x, y = new_im.size
    return new_im


def process_image(img):
    """
    Calls the make_square method and returns an instagram formatted, ready to upload image.
    """

    new_img = make_square(img)
    return new_img
