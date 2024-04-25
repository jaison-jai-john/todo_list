import os
import random
import string

from PIL import Image, ImageDraw, ImageFont


def captcha_auth():

    # using random.choices()
    # generating random strings
    code = "".join(random.choices(string.ascii_uppercase + string.digits, k=7))

    # create a new image
    image = Image.new("RGB", (125, 45), (255, 255, 255))

    # draw a random string of characters on the image
    draw = ImageDraw.Draw(image)
    font = ImageFont.truetype("arial.ttf", 20)
    draw.text((10, 10), code, font=font, fill=(0, 0, 0))

    # save the image to a file
    image.save("captcha.png")

    # display the CAPTCHA to the user
    captcha = Image.open("captcha.png")
    captcha.show()

    # ask the user to enter the text that they see
    text = input("Enter the text in the image or regenerate/ exit: ").upper()
    # check if the user entered the correct text
    if text == code:
        return True
    elif text == "REGENERATE":
        return captcha_auth()
    elif text == "EXIT":
        exit()
    else:
        return False
    captcha.close()
    os.remove("captcha.png")
