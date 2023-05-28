from PIL import Image, ImageDraw, ImageFont
from io import BytesIO

def individualism(ORIGINAL, discriminator=None, custom=None, avatar=None):
    if discriminator is not None:
        TEXT = f'"{discriminator}번은 개인 주의야."'
    if custom is not None:
        TEXT = custom
    FONT = './Font.ttf'
    colorText = (255,255,255,255)
    colorOutline = (0,0,0,255)
    colorShadow = (0,0,0,90)
    outlineAmount = 5
    shadowX = 9
    shadowY = 6
    waterMarkHeightRatio = 0.06
    imgSrc = Image.open(ORIGINAL).convert("RGBA")
    imgSrc = imgSrc.resize((1920, 1080))
    imgOutput = Image.new("RGBA", imgSrc.size)
    fontSize = round(imgSrc.height * waterMarkHeightRatio)
    if avatar is not None:
        avatar = Image.open(avatar)
        avatar = avatar.resize((350, 350))
        imgOutput.paste(im=avatar, box=(500, 100))
    fontWatermark = ImageFont.truetype(font=FONT, size=fontSize)
    fontWidth,fontHeight = fontWatermark.getsize(TEXT)
    offsetX = int((imgSrc.width / 2) - (fontWidth / 2))
    offsetY = int(imgSrc.height * 0.12)
    WatermarkStartX = imgSrc.width - fontWidth - offsetX
    WatermarkStartY = imgSrc.height - fontHeight - offsetY

    for x in range(-outlineAmount + shadowX, outlineAmount + shadowX + 1):
        for y in range(-outlineAmount + shadowY, outlineAmount + shadowY + 1):
            if x == 0 and y == 0:
                continue
            if abs(x) == outlineAmount or abs(y) == outlineAmount:
                color = colorOutline
            else:
                color = colorShadow
            ImageDraw.Draw(imgOutput).text((WatermarkStartX + x, WatermarkStartY + y), TEXT,
                                           fill=color,
                                           font=fontWatermark)

    ImageDraw.Draw(imgOutput).text((WatermarkStartX + shadowX,
                                    WatermarkStartY + shadowY),
                                   TEXT,
                                   fill=colorShadow,
                                   font=fontWatermark)

    ImageDraw.Draw(imgOutput).text((WatermarkStartX,
                                    WatermarkStartY),
                                   TEXT,
                                   fill=colorText,
                                   font=fontWatermark)

    buf = BytesIO()
    out = Image.alpha_composite(imgSrc, imgOutput)
    out.convert('RGB').save(buf, 'png')
    buf.seek(0)
    return buf


if __name__ == "__main__":
    buf = individualism("./개인주의.png", discriminator="4")
    open("sans.png", "wb").write(buf.read())
