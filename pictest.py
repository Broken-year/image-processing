"""
图像处理
"""
"""
RGB颜色,3个颜色通道组成
红 255,0,0
绿 0,255,0
蓝 0,0,255

黄 255,255,0

一个像素pixel =3字节
"""
from PIL import Image
#模糊处理
from PIL import ImageFilter
#合成模块
from PIL import ImageChops
#色彩亮度调整
from PIL import ImageEnhance
#绘制图像
from PIL import ImageDraw,ImageFont


def main():
    im = Image.open('./kfc/kfc-1.png')
    #显示图片
    #im.show()

    #获取图片格式
    print(im.format)

    #获取图片大小
    print(im.size)

    #获得高度和宽度
    print(im.height,im.width)
    #获取某个像素的颜色
    print(im.getpixel((163,52)))
    print('------------------')

    """
    图片混合和遮罩处理
    """
    # im1 = Image.open("./kfc/kfc-1.png").convert(mode='RGB')
    # im2 = Image.new('RGB',im1.size,'green')
    # #混合
    # Image.blend(im1,im2,alpha=0.5).show()

    # im1 = Image.open("./kfc/kfc-1.png")
    # im2 = Image.open("./kfc/kfc-2.png")
    #
    # #重新让图片变小
    # im2 = im2.resize(im1.size)
    # r,g,b = im2.split()
    # #遮罩处理
    # Image.composite(im2,im1,r).show()


    """
    复制,缩放,镜像
    """
    im1=Image.open('./kfc/kfc-1.png')
    im2 = Image.open("./kfc/kfc-2.png")
    #把每个像素扩大两倍
    #Image.eval(im1,lambda i:i*2).show()

    # #复制一个图片副本到内存
    # copy = im1.copy()
    # #缩放到指定大小
    # copy.thumbnail((100,50))
    # copy.show()

    # #剪切图片
    # part1 = im1.crop((5,5,130,130))
    # #粘贴图片
    # im2.paste(part1,(30,30))
    # im2.show()

    #逆时针90°
    #im1.rotate(90).show()

    #左右镜像
    #im1.transpose(Image.FLIP_LEFT_RIGHT).show()

    #上下镜像
    # im1.transpose(Image.FLIP_TOP_BOTTOM).show()

    #旋转90°
    # im1.transpose(Image.ROTATE_90).show()

    #颠倒
    # im1.transpose(Image.TRANSPOSE).show()

    """
    图片通道分离和滤镜
    """
    im2 = im2.resize(im1.size)

    #进行rgb分离
    r1,g1,b1 = im1.split()
    r2,g2,b2 = im2.split()

    #制作合成一个新图片
    tmp1 = [r1,g2,b1]
    im3 = Image.merge('RGB',tmp1)
    #im3.show()

    #高斯模糊
    # im2.filter(ImageFilter.GaussianBlur).show()

    #图片进行加法运算
    # ImageChops.add(im1,im2).show()

    #图片减法运算
    # ImageChops.subtract(im1,im2).show()

    #图片变暗(图片保留较暗部分)
    # ImageChops.darker(im1,im2).show()

    #图片变亮
    # ImageChops.lighter(im1,im2).show()

    #图片叠加
    # ImageChops.multiply(im1,im2).show()

    #同时显示到屏幕上
    # ImageChops.screen(im1,im2).show()

    #图片变成底片
    # ImageChops.invert(im1).show()

    #图片取不同
    # ImageChops.difference(im1,im2).show()

    #保存
    # im2.save("./kfc/haha.png")

    w,h = im1.size
    #设置新的图片,宽度为3张原图
    image_output = Image.new('RGB',((3*w),h))
    #第一张防原图
    image_output.paste(im1,(0,0))

    #第二张放增强图
    img_color = ImageEnhance.Color(im1)
    #把图片增强
    imga = img_color.enhance(1.5)
    image_output.paste(imga,(w,0))

    #第三张防减弱的图
    imgb = img_color.enhance(0.5)
    image_output.paste(imgb,(2*w,0))

    # image_output.show()

    #亮度调整
    img_color = ImageEnhance.Brightness(im1)
    image1 = img_color.enhance(2.1)
    # image1.show()

    #创建一个300x250的白色底面图像
    pic = Image.new('RGB',(300,250),'white')
    #选择图片资源去画画
    draw_obj = ImageDraw.Draw(pic)
    #绘制一个红色矩形
    draw_obj.rectangle((50,50,150,150),fill='blue',outline='red')
    #绘制文本
    font = ImageFont.truetype('./test.TTF',20)
    draw_obj.text((100,100),'中国文化博大精深',font=font,fill='green')

    #画一个圆
    draw_obj.arc((0,0,100,50),0,180,fill='blue')

    #画一条线
    draw_obj.line((0,0,20,30),fill=128,width=1)

    #画一个十字架
    draw_obj.line((0,0)+pic.size,fill=128,width=5)
    draw_obj.line((0,pic.size[1],pic.size[0],0),fill=128,width=5)
    pic.show()
    pass


if __name__ == '__main__':
    main()