from PIL import Image, ImageDraw, ImageFont 
def edit_image(text, size, x, y, imagepath, outputimage):
    # Load an image
    image = Image.open(imagepath)

    # Create a drawing object
    draw = ImageDraw.Draw(image)

    # Define the text and font
    try:
        font = ImageFont.truetype("arial.ttf", size)
    except IOError:
        font = ImageFont.load_default()

    # Define text position
    position = (x, y)

    # Draw the text on the image
    draw.text(position, text, fill="white", font=font)

    # Save the image with the text
    image.save(f'{outputimage}')