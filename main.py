from PIL import Image
from PIL import ImageFont
from PIL import ImageDraw

target_image = Image.open(r"IMG_0981.jpeg")
new_size = (800, 600)
target_image = target_image.resize(new_size)
target_image.show()

watermark_image = target_image.copy()
draw = ImageDraw.Draw(watermark_image)
# font = ImageFont.load_default()
font = ImageFont.truetype("/Library/fonts/Arial.ttf", 30)

# add watermark
draw.text((0, 0), "Copyright - PZ SS", (255, 255, 255), font=font)
watermark_image.show()
