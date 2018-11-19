'''PIL (Python Image Library)
As a matter of fact, it has already become the standard
module dealing with images.
Module PIL is very powerful, but the API is very easy to use.

More details at
http://effbot.org/imagingbook/
'''
print(__doc__)
from PIL import Image, ImageFilter, ImageDraw, ImageFont
import random

def snacks():
    i = Image.open('zhihu.png')
    w, h = i.size
    # thumbnail it, pass into a tuple obj
    i.thumbnail((w // 2, h // 2))
    # save the image as jpeg
    i = i.filter(ImageFilter.BLUR)
    i.save('thumbnail.jpg', 'png')

def main():
    # random character
    def rndChar():
        return chr(random.randint(65, 90))

    # random color1
    def rndColor():
        return (random.randint(64, 255), random.randint(64, 255), random.randint(64, 255))

    # randmo color2
    def rndColor2():
        return (random.randint(32, 127), random.randint(32, 127), random.randint(32, 127))

    width = 60 * 4
    height = 60
    image = Image.new('RGB', (width, height), (255, 255, 255))
    font = ImageFont.truetype('Arial.ttf', 36)
    draw = ImageDraw.Draw(image)
    for x in range(width):
        for y in range(height):
            draw.point((x, y), fill=rndColor())

    for t in range(4):
        draw.text((60 * t + 10, 10), rndChar(), font=font, fill=rndColor2())
    image = image.filter(ImageFilter.BLUR)
    image.save('code.jpg', 'jpeg')

main()
