"""
验证码
"""
import random

from PIL import Image
#绘制图像
from PIL import ImageDraw,ImageFont

pic = Image.new('RGB',(300,250),'white')
draw_obj = ImageDraw.Draw(pic)

#获得随机颜色
def get_color():
    return (random.randint(200,255),random.randint(200,255),random.randint(200,255))

#生成随机字母
def get_char():
    return chr(random.randint(65,97))

def main():

    #每个像素都花点
    for x in range(300):
        for y in range(250):
            draw_obj.point((x,y),fill=get_color())

    #干扰线
    for i in range(2):
        draw_obj.line(((10,10),(80,80)),fill=(0,250,0),width=3)

    #生成随机字母
    for i in range(4):
        draw_obj.text((10+i*20,50),get_char(),fill=(255,0,0))

    pic.show()


    pass
if __name__ == '__main__':
    main()