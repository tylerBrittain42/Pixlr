from audioop import avg
from operator import le
from PIL import Image
import math


def main():
    checker = Image.open('./sample/checker.jpeg')
    # pix = checker.load()
    # foo = checker.split()
    # print(pix[0,0])
    
    
    # print(im.size[0])

    avg_color = average_pix(checker)
    print(avg_color)




# https://sighack.com/post/averaging-rgb-colors-the-right-way
def average_pix(im):

    # counters
    red = 0
    green = 0
    blue = 0

    # init setup
    pixels = im.load()
    width = im.width
    height = im.height
    total_pix = width * height

    # gathering color totals
    for x in range(0,width):
        for y in range(0,height):
            # print(pixels[x,y])
            red += pixels[x,y][0]
            green += pixels[x,y][1]
            blue += pixels[x,y][2]
    
    # calculating average
    avg_squared = [red**2, green**2, blue**2]
    avg_rt =list(map(lambda x: math.sqrt(x)//total_pix, avg_squared))
    
    return(avg_rt)


    



if __name__ == '__main__':
    main()