from PIL import Image, ImageDraw, ImageFont

W, H = 1600, 1200
img = Image.new("RGB", (W, H), (245, 247, 250))
draw = ImageDraw.Draw(img)

bold = "/usr/share/fonts/truetype/liberation/LiberationSans-Bold.ttf"
reg = "/usr/share/fonts/truetype/liberation/LiberationSans-Regular.ttf"

title_font = ImageFont.truetype(bold, 86)
sub_font = ImageFont.truetype(reg, 44)
name_font = ImageFont.truetype(reg, 36)

text_color = (20, 20, 25)

title_l1 = "Why do diets no longer deliver"
title_l2 = "results after 35?"
subtitle = "Hormones – metabolism – energy – sustainable fat loss"

def center_x(text, font):
    bbox = draw.textbbox((0, 0), text, font=font)
    return (W - (bbox[2] - bbox[0])) // 2

y = 230
draw.text((center_x(title_l1, title_font), y), title_l1, font=title_font, fill=text_color)
y += 110
draw.text((center_x(title_l2, title_font), y), title_l2, font=title_font, fill=text_color)

y += 180
draw.text((center_x(subtitle, sub_font), y), subtitle, font=sub_font, fill=text_color)

y += 240
lines = [
    "Selma Nuhija-Kerić",
    "Certified FASTer Way to Fat Loss Coach",
    "Working with women 35+",
]
for line in lines:
    draw.text((center_x(line, name_font), y), line, font=name_font, fill=text_color)
    y += 56

img.save("/home/user/Shramba/slide_en.png")
print("saved")
