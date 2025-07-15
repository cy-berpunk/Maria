from PIL import Image, ImageDraw, ImageFont
import random

image_path = "maria.jpg"
image = Image.open(image_path)

draw = ImageDraw.Draw(image)

try:
    font = ImageFont.truetype("msgothic", size=30)
except:
    font = ImageFont.load_default()

txet = ["汝の敵を愛せよ", "富は天の国に積め", "貧しい者は幸いである"]
position = (100, 650)
text_color = (255, 255, 255)

draw.text(position, random.choice(txet), fill=text_color, font=font)

image.show()