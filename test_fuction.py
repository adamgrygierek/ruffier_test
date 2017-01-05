from PIL import Image, ImageFilter
import pytesseract
import re

image = Image.open('SHealth_20_57_14_614.png')
width, height = image.size
left = 300
top = 200
right = width - 400  # / 2
bottom = height - 700  # / 2
image = image.crop((left, top, right, bottom))
image.show()
# img = image.filter(ImageFilter.BLUR)
# img.show()
value = (pytesseract.image_to_string(image))
#    value = int(value[:-7])
intigers = [int(s) for s in value.split() if s.isdigit()]
smth = [int(s) for s in re.findall(r'\b\d+\b', value)]
print int(filter(str.isdigit, value))
print value
print smth
