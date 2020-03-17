import os
from PIL import Image
def main():
    i = 258
    for filename in os.listdir("./test"):
        if '.jpg' in filename:
            src='test/'+filename
            nm=str(i)+'.jpg'
            retu = resizeImg(src, str(i))

            i+= 1
        elif '.png' in filename:
            src='test/'+filename
            nm=str(i)+'.png'
            retu = resizeImg(src, str(i))

            i+= 1
        elif '.mp4' in filename:
            pass

        else:
            pass
def resizeImg(img_n, name):
    img = Image.open(img_n)
    img_w, img_h = img.size

    if img_w > img_h:
        nw = 1080
        nh = round(nw*img_h/img_w)
        print ("Width bigger")
    else:
        nh = 1080
        nw = round(nh*img_w/img_h)
    resized_im = img.resize((nw, nh))
    background = Image.new('RGB', (1080, 1080), (255, 255, 255, 255))
    bg_w, bg_h = background.size
    offset = ((bg_w - nw) // 2, (bg_h - nh) // 2)
    background.paste(resized_im, offset)
    newname = name + '.jpg'
    background.save(newname)
    return newname



if __name__ == '__main__':
    main()
