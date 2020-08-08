from PIL import Image 
from PIL import ImageDraw 
from PIL import ImageFont
from io import BytesIO


def individualism(ORIGINAL, discriminator=None, custom=None, avatar=None):
    if discriminator is not None:
        TEXT = f'"{discriminator}번은 개인 주의야."'
    if custom is not None:
        TEXT = custom
    
    FONT = './Font.ttf'

    colorText = (255,255,255,255)  # 워터마크 텍스트 색깔
    colorOutline = (0,0,0,255)  # 테두리 색깔
    colorShadow = (0,0,0,90)  # 그림자 색깔
    outlineAmount = 5  # 테두리 두께
 
    shadowX = 9  # 그림자 X 위치
    shadowY = 6  # 그림자 Y 위치
 
    waterMarkHeightRatio = 0.06  # 크기 비율
 
    imgSrc = Image.open(ORIGINAL).convert("RGBA")  # 원본 이미지 오픈
    imgSrc = imgSrc.resize((1920, 1080))
    imgOutput = Image.new("RGBA", imgSrc.size)  # 이미지 생성
    fontSize = round(imgSrc.height * waterMarkHeightRatio)  # 폰트 사이즈 확인

    if avatar is not None:
        avatar = Image.open(avatar)
        avatar = avatar.resize((350, 350))
        imgOutput.paste(im=avatar, box=(500, 100))

    fontWatermark = ImageFont.truetype(font=FONT, size = fontSize)
    fontWidth,fontHeight = fontWatermark.getsize(TEXT)
 
    offsetX = int((imgSrc.width / 2) - (fontWidth / 2))
    offsetY = int(imgSrc.height * 0.12)
 
    posWatermarkStartX = imgSrc.width - fontWidth - offsetX
    posWatermarkStartY = imgSrc.height - fontHeight - offsetY
 
    # 그림자
    ImageDraw.Draw(imgOutput).text( (posWatermarkStartX - outlineAmount +shadowX, posWatermarkStartY +shadowY ), TEXT,fill=colorShadow, font=fontWatermark) 
    ImageDraw.Draw(imgOutput).text( (posWatermarkStartX + outlineAmount +shadowX, posWatermarkStartY +shadowY), TEXT,fill=colorShadow, font=fontWatermark) 
    ImageDraw.Draw(imgOutput).text( (posWatermarkStartX +shadowX, posWatermarkStartY - outlineAmount +shadowY), TEXT,fill=colorShadow, font=fontWatermark) 
    ImageDraw.Draw(imgOutput).text( (posWatermarkStartX +shadowX, posWatermarkStartY + outlineAmount +shadowY), TEXT,fill=colorShadow, font=fontWatermark) 
    ImageDraw.Draw(imgOutput).text( (posWatermarkStartX - outlineAmount +shadowX, posWatermarkStartY - outlineAmount +shadowY), TEXT,fill=colorShadow, font=fontWatermark) 
    ImageDraw.Draw(imgOutput).text( (posWatermarkStartX + outlineAmount +shadowX, posWatermarkStartY - outlineAmount +shadowY), TEXT,fill=colorShadow, font=fontWatermark) 
    ImageDraw.Draw(imgOutput).text( (posWatermarkStartX - outlineAmount +shadowX, posWatermarkStartY + outlineAmount +shadowY), TEXT,fill=colorShadow, font=fontWatermark) 
    ImageDraw.Draw(imgOutput).text( (posWatermarkStartX + outlineAmount +shadowX, posWatermarkStartY + outlineAmount +shadowY), TEXT,fill=colorShadow, font=fontWatermark) 
    ImageDraw.Draw(imgOutput).text( (posWatermarkStartX+shadowX, posWatermarkStartY+shadowY ), TEXT,fill=colorShadow, font=fontWatermark)
 
    # 테두리
    ImageDraw.Draw(imgOutput).text( (posWatermarkStartX - outlineAmount, posWatermarkStartY ), TEXT,fill=colorOutline, font=fontWatermark) 
    ImageDraw.Draw(imgOutput).text( (posWatermarkStartX + outlineAmount, posWatermarkStartY ), TEXT,fill=colorOutline, font=fontWatermark) 
    ImageDraw.Draw(imgOutput).text( (posWatermarkStartX, posWatermarkStartY - outlineAmount ), TEXT,fill=colorOutline, font=fontWatermark) 
    ImageDraw.Draw(imgOutput).text( (posWatermarkStartX, posWatermarkStartY + outlineAmount ), TEXT,fill=colorOutline, font=fontWatermark) 
    ImageDraw.Draw(imgOutput).text( (posWatermarkStartX - outlineAmount, posWatermarkStartY - outlineAmount ), TEXT,fill=colorOutline, font=fontWatermark) 
    ImageDraw.Draw(imgOutput).text( (posWatermarkStartX + outlineAmount, posWatermarkStartY - outlineAmount ), TEXT,fill=colorOutline, font=fontWatermark) 
    ImageDraw.Draw(imgOutput).text( (posWatermarkStartX - outlineAmount, posWatermarkStartY + outlineAmount ), TEXT,fill=colorOutline, font=fontWatermark) 
    ImageDraw.Draw(imgOutput).text( (posWatermarkStartX + outlineAmount, posWatermarkStartY + outlineAmount ), TEXT,fill=colorOutline, font=fontWatermark) 
 
    # 메인 텍스트
    ImageDraw.Draw(imgOutput).text( (posWatermarkStartX, posWatermarkStartY ), TEXT,fill=colorText, font=fontWatermark) 
 
    buf = BytesIO()

    out = Image.alpha_composite(imgSrc, imgOutput)
    out.convert('RGB').save(buf, 'png')

    buf.seek(0)
    return buf

if __name__ == "__main__":
    buf = individualism("./개인주의.png", discriminator="4")
    open("sans.png", "wb").write(buf.read())